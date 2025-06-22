from django.db import models

# Create your models here.
class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null = True,blank= True)
    name = models.CharField(max_length=255)
    description = models.TextField(null = True,blank= True)
    time = models.IntegerField(null=True,blank= True)

    def toDict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'time': self.time,
        }

class QuestionSet(models.Model):
    id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_id = models.IntegerField ()

    def toDict(self):
        return {
            'id': self.id,
            'exam_id': self.exam_id,
            'question_id': self.question_id,
        }

