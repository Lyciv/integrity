import json
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app_student.models import Student
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
