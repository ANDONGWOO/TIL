
from django.urls import path
from . import views

app_name='member'

urlpatterns = [
    path('',views.main, name='main'),#메인
    path('accounts/signup',views.create, name='create'),#회원가입
    path('accounts/',views.index, name='index'),#회원목록
    path('accounts/<pk>',views.detail, name='detail'),#회원정보 조회
    path('accounts/login/',views.login, name='login'),#로그인
    path('accounts/logout/',views.logout, name='logout'),#로그아웃
    path('accounts/<pk>/update',views.update, name='update'),#회원정보 수정
]