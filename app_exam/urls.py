from django.urls import path

from app_exam.views import create_exam, update_exam, add_question, show_exam, show_question, show_question_for_student, \
    show_all_exam

app_name='exam'

urlpatterns = [
    path('create', create_exam),
    path('update', update_exam),
    path('add', add_question),
    path('show', show_exam),
    path('question', show_question),
    path('student', show_question_for_student),
    path('all', show_all_exam),
]