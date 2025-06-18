from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    column_id = models.IntegerField(null=True,blank=False)
    user_id = models.IntegerField(null=True,blank=False)
    title = models.CharField(max_length=50,null=True,blank=False)
    content = models.TextField(null=True,blank=False)
    photo_url = models.CharField(max_length=100,null=True,blank=False)
    video_id = models.CharField(max_length=50,null=True,blank=False)
    # deleted alive
    status = models.CharField(max_length=10,null=True,blank=False)
    create_time = models.DateTimeField(auto_now_add=True,null=True,blank=False)
    update_time = models.DateTimeField(auto_now=True,null=True,blank=False)
