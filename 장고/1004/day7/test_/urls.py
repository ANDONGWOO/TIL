
from django.urls import path
from . import views

app_name = "day7"#앱이름

urlpatterns = [
    #test_/ 기본 
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
]
