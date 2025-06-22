import os
import uuid

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from main import settings
from utils.auth import token_auth


# Create your views here.

@csrf_exempt
# @token_auth
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
                "data": os.path.join(settings.MEDIA_URL, 'uploads',new_file_name)  # 或返回数据库路径等
            })
        except Exception as e:
            return JsonResponse({"code": 500, "message": "上传失败",'data':e})
