from django.urls import path

from app_student.views import student_info, student_update

app_name='student'

urlpatterns = [
    path('info', student_info),
    path('update', student_update),
]
