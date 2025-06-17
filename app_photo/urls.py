from django.urls import path

from app_photo.views import upload

app_name='photo'

urlpatterns = [
    path('upload', upload),
]