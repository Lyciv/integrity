import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app_column.models import Column
from app_question.models import Question
from utils.auth import token_teacher


# Create your views here.
@csrf_exempt
@token_teacher
def add_question(request):
    if request.method == "POST":
        req = json.loads(request.body)
        try:
            column=Column.objects.get(id=req['column_id'])
            question=Question(
                question_text=req['text'],
                column_id=req['column_id'],
                a=req['a'],
                b=req['b'],
                c=req['c'],
                d=req['d'],
                answer=req['answer']
            )
            question.save()
            return JsonResponse({"code": "200", "msg": "添加成功。",'data':question.toDict()})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "添加失败。", "data": str(e)})

@csrf_exempt
@token_teacher
def update_question(request):
    if request.method == "POST":
        req = json.loads(request.body)
        try:
            question=Question(id=req['id'],
                              question_text=req['text'],
                              column_id=req['column_id'],
                              a=req['a'],
                              b=req['b'],
                              c=req['c'],
                              d=req['d'],
                              answer=req['answer']
                              )
            question.save()
            return JsonResponse({"code": "200", "msg": "修改成功。",'data':question.toDict()})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "修改失败。", "data": str(e)})

@csrf_exempt
@token_teacher
def show_single_question(request):
    if request.method == "POST":
        req = json.loads(request.body)
        try:
            question=Question.objects.get(id=req['id'])
            return JsonResponse({"code": "200", "msg": "查询成功。",'data':question.toDict()})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "查询失败。", "data": str(e)})

@csrf_exempt
@token_teacher
def show_question_list(request):
    if request.method == "POST":
        req = json.loads(request.body)
        try:
            question_list=Question.objects.filter(column_id=req['column_id'])
            return JsonResponse({"code": "200", "msg": "查询成功。",'data':[question.toDict() for question in question_list]})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "查询失败。", "data": str(e)})