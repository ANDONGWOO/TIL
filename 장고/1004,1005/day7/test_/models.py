from django.db import models

# Create your models here.

class Test(models.Model):#클래스 정의
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)