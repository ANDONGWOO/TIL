from django.db import models

# Create your models here.

class  Movie(models.Model):
    title = models.CharField(max_length=50)# 글자수 50까지
    summary = models.TextField()
    running_time = models.TimeField()#???