import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app_exam.models import Exam, QuestionSet
from app_question.models import Question
from utils.auth import token_teacher, token_auth, token_student
from utils.token import teacher_token


# Create your views here.
@csrf_exempt
# @token_teacher
def create_exam(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        try:
            # user_id=teacher_token(request.META.get("HTTP_X_TOKEN", b''))['result']['data']['uid']
            exam1=Exam.objects.filter(name=req['name'])
            if exam1:
                return JsonResponse({"code": "500", "msg": "考试已存在"})
            exam=Exam(
                name=req['name'],
                # user_id=user_id,
                description=req['description'],
                time=req['time'],
            )
            exam.save()
            return JsonResponse({"code": "200", "msg": "创建成功","data": exam.toDict()})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "创建失败", "error": str(e)})

@csrf_exempt
@token_teacher
def update_exam(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        try:
            user_id=teacher_token(request.META.get("HTTP_X_TOKEN", b''))['result']['data']['uid']
            exam=Exam.objects.filter(id=req['id'], user_id=user_id)
            if not exam:
                return JsonResponse({"code": "500", "msg": "考试不存在"})
            exam=Exam(
                id=req['id'],
                name=req['name'],
                description=req['description'],
                time=req['time'],
            )
            return JsonResponse({"code": "200", "msg": "更新成功","data": exam.toDict()})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "更新失败", "error": str(e)})

@csrf_exempt
# @token_teacher
def add_question(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        try:
            exam=Exam.objects.get(id=req['exam_id'])
            question=Question.objects.filter(id=req['question_id'])
            if question:
                question_set=QuestionSet.objects.filter(exam_id=req['exam_id'], question_id=req['question_id'])
                if question_set:
                    return JsonResponse({"code": "500", "msg": "题目已存在"})
                question_set=QuestionSet(
                    exam=exam,
                    question_id=req['question_id']
                )
                question_set.save()
                return JsonResponse({"code": "200", "msg": "添加成功", "data": question_set.toDict()})
            else:
                return JsonResponse({"code": "500", "msg": "题目不存在"})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "添加失败", "error": str(e)})

@csrf_exempt
@token_teacher
def show_exam(request):
    if request.method == 'GET':
        try:
            user_id=teacher_token(request.META.get("HTTP_X_TOKEN", b''))['result']['data']['uid']
            exam_list=Exam.objects.filter(user_id=user_id)
            return JsonResponse({"code": "200", "msg": "查询成功", "data": [exam.toDict() for exam in exam_list]})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "查询失败", "error": str(e)})

@csrf_exempt
# @token_teacher
def show_question(request):
    if request.method == 'POST':
        req=json.loads(request.body)
        try:
            exam_id=req['exam_id']
            question_list=QuestionSet.objects.filter(exam_id=exam_id)
            question=[]
            for i in question_list:
                question.append(Question.objects.get(id=i.question_id))
            return JsonResponse({"code": "200", "msg": "查询成功", "data": [q.toDict() for q in question]})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "查询失败", "error": str(e)})

@csrf_exempt
# @token_student
def show_question_for_student(request):
    if request.method == 'POST':
        req=json.loads(request.body)
        try:
            exam_id=req['exam_id']
            question_list=QuestionSet.objects.filter(exam_id=exam_id)
            question=[]
            for i in question_list:
                question.append(Question.objects.get(id=i.question_id))
            return JsonResponse({"code": "200", "msg": "查询成功", "data": [q.toDict2() for q in question]})
        except Exception as e:
            return JsonResponse({"code": "500", "msg": "查询失败", "error": str(e)})

@csrf_exempt
def show_all_exam(request):
    if request.method=='GET':
        exams=Exam.objects.all()
        return JsonResponse({"code": "200", "msg": "查询成功", "data": [exam.toDict() for exam in exams]})