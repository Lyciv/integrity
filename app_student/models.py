from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=20,null=True,blank=False)
    number = models.CharField(max_length=20,null=True,blank=False)
    telephone = models.CharField(max_length=20,null=True,blank=False)
    college = models.CharField(max_length=50,null=True,blank=False)
    url = models.CharField(max_length=100,null=True,blank=False)  # 图片地址

    def toDict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'number': self.number,
            'telephone': self.telephone,
            'college': self.college,
            'url': self.url
        }