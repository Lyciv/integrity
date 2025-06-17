from django.urls import path

from app_student.views import student_info

app_name='student'

urlpatterns = [
    path('info', student_info)
]
