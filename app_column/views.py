import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app_column.models import Column


# Create your views here.
@csrf_exempt
def search_column(request):
    if request.method=='POST':
        try:
            req=json.loads(request.body)
            column=Column.objects.get(name=req["name"])
            return JsonResponse({"code":"200","data":column.toDict(),"msg":"查询成功"})
        except Exception as e:
            return JsonResponse({"code":"400","data":None,"msg":str(e)})

@csrf_exempt
def add_column(request):
    if request.method=='POST':
        try:
            req=json.loads(request.body)
            if len(Column.objects.filter(name=req["name"]))!=0:
                return JsonResponse({"code":"400","data":None,"msg":"已存在同名专栏"})
            column=Column(name=req["name"],description=req["description"])
            column.save()
            return JsonResponse({"code":"200","data":column.toDict(),"msg":"添加成功"})
        except Exception as e:
            return JsonResponse({"code":"400","data":None,"msg":str(e)})
@csrf_exempt
def add_column(request):
    if request.method=='POST':
        try:
            req=json.loads(request.body)
            if len(Column.objects.filter(name=req["name"]))!=0:
                return JsonResponse({"code":"400","data":None,"msg":"已存在同名专栏"})
            column=Column(name=req["name"],description=req["description"])
            column.save()
            return JsonResponse({"code":"200","data":column.toDict(),"msg":"添加成功"})
        except Exception as e:
            return JsonResponse({"code":"400","data":None,"msg":str(e)})

@csrf_exempt
def show_column(request):
    if request.method=='GET':
        try:
            columns=Column.objects.all()
            data=[column.toDict() for column in columns]
            return JsonResponse({"code":"200","data":data,"msg":"查询成功"})
        except Exception as e:
            return JsonResponse({"code":"400","data":None,"msg":str(e)})