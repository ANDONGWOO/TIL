
from django.urls import path
from . import views

app_name= "signup"

urlpatterns = [
    path('',views.main, name='main'),#메인
    path('signup/',views.index, name='index'),#목록 조회
    path('signup/signup/',views.create, name='create'),#회원 가입
    path('signup/<int:user_pk>/',views.detail, name='detail'),#목록 조회name 클릭시
]