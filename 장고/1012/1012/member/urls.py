
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/signup', views.create, name='create'),#회원가입
    path('accounts/', views.index, name='index'),#목록
    path('accounts/<int:pk>', views.detail, name='detail'),#조회
    path('accounts/login', views.login, name='login'),#로그인
    # path('accounts/logout', views.logout, name='logout'),#로그인
]