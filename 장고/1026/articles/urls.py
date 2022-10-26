from django.urls import path
from . import views

app_name= 'articles'
urlpatterns = [
    path('', views.index, name="index"),#목록 조회
    path('create/', views.create, name="create"),# 게시글 생성
    path('<int:articles_pk>/', views.detail, name="detail"),#게시글 정보 조회
    path('<int:articles_pk>/comments/', views.comments_create, name="comments_create"),#댓글 생성 비동기
    path('<int:articles_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name="comments_delete"),#댓글 삭제 비동기
]