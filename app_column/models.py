from django.db import models

# Create your models here.
class Column(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }