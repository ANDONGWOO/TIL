from django.contrib import admin
from.models import Article, Comment#모델
# Register your models here.

admin.site.register(Article) 
admin.site.register(Comment) 
#관리자 페이지에 모델 등록