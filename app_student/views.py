import json
import os
import uuid

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app_student.models import Student
from main import settings
from main.settings import MEDIA_URL
from utils.auth import token_student
from utils.token import student_token


@csrf_exempt
@token_student
def student_info(request):
    if request.method == 'GET':
        try:
            user_id=student_token(request.META.get("HTTP_X_TOKEN", b''))['result']['data']['uid']
            student=Student.objects.get(user_id=user_id)
            student.url=os.path.join(MEDIA_URL, 'uploads',student.url)
            if student:
                return JsonResponse({"code": "200", "msg": "成功", "data": {"student": student.toDict()}})
            else:
                return JsonResponse({"code": "400", "msg": "失败，参数错误。"})
        except Exception as err:
            return JsonResponse({"code": "500", "msg": "失败，参数错误。", "en_msg": str(err)})
    elif request.method == 'POST':
        try:
            user_id=student_token(request.META.get("HTTP_X_TOKEN", b''))['result']['data']['uid']
            req=json.loads(request.body)
            student=Student.objects.get(user_id=user_id)
            student=Student(
                id=student.id,
                user_id=user_id,
                name=req['name'],
                number=req['number'],
                telephone=req['telephone'],
                college=req['college'],
                url=req['url'].split('\\')[-1],
            )
            student.save()
            return JsonResponse({"code": "200", "msg": "成功", "data": {"student": student.toDict()}})
        except Exception as err:
            return JsonResponse({"code": "500", "msg": "失败，参数错误。", "en_msg": str(err)})



@csrf_exempt
@token_student
def upload(request):
    if request.method == "POST":
        try:
            # 获取上传的文件对象
            uploaded_file = request.FILES.get("file")
            if not uploaded_file:
                return JsonResponse({"code": 400, "message": "未接收到文件"})

            # 使用 uuid 生成唯一文件名
            file_name, file_extension = os.path.splitext(uploaded_file.name)
            new_file_name = f"{uuid.uuid4()}{file_extension}"

            # 构建存储路径
            upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads')  # 可选：自定义子目录
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)

            # 文件在服务器上的完整路径
            file_path = os.path.join(upload_path, new_file_name)

            # 写入文件
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return JsonResponse({
                "code": 200,
                "message": "OK",
                "data": upload_path.join(new_file_name)  # 或返回数据库路径等
            })
        except Exception as e:
            return JsonResponse({"code": 500, "message": "上传失败",'data':e})
