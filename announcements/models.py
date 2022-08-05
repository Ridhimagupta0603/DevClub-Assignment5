from django.db import models
from Users.models import *
# Create your models here.
class announcement(models.Model):
    announcement=models.CharField(max_length=255,null=True)
    posted_by=models.CharField(max_length=255,null=True)
    course=models.CharField(max_length=255,null=True)
    title=models.CharField(max_length=255,null=True)
    
    def __str__(self):
        return self.title
