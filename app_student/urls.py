from django.urls import path

from app_student.views import upload, student_info

app_name='student'

urlpatterns = [
    path('upload', upload),
    path('info', student_info)
]
