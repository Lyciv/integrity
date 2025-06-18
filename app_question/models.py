from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    column_id = models.IntegerField(null= True, blank=True)
    question_text = models.CharField(max_length=200, null= True, blank=True)
    a = models.CharField(max_length=200, null= True, blank=True)
    b = models.CharField(max_length=200, null= True, blank=True)
    c = models.CharField(max_length=200, null= True, blank=True)
    d = models.CharField(max_length=200, null= True, blank=True)
    answer = models.CharField(max_length=200, null= True, blank=True)

    def toDict(self):
        return {
            'id': self.id,
            'column_id': self.column_id,
            'question_text': self.question_text,
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d,
            'answer': self.answer
        }