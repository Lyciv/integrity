import json
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app_student.models import Student
from main.settings import MEDIA_URL
from utils.auth import token_student
from utils.token import student_token


@csrf_exempt
# @token_student
def student_info(request):
    if request.method == 'POST':
        try:
            req=json.loads(request.body)
            student=Student.objects.get(username=req["username"])
            student.url=os.path.join(MEDIA_URL, 'uploads',student.url)
            if student:
                return JsonResponse({"code": "200", "msg": "成功", "data": {"student": student.toDict()}})
            else:
                return JsonResponse({"code": "400", "msg": "失败，参数错误。"})
        except Exception as err:
            return JsonResponse({"code": "500", "msg": "失败，参数错误。", "en_msg": str(err)})

@csrf_exempt
def student_update(request):
    if request.method == 'POST':
        try:
            req=json.loads(request.body)
            username=req['username']
            student=Student.objects.filter(username=username)
            if len(student)==0:
                student=Student(
                    username=username,
                    name=req['name'],
                    number=req['number'],
                    telephone=req['telephone'],
                    college=req['college'],
                    url=req['url'].split('\\')[-1],
                )
                student.save()
                return JsonResponse({"code": "200", "data": student, "msg": "查询成功"})
            student=Student.objects.get(username=username)
            student=Student(
                id=student.id,
                username=username,
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
