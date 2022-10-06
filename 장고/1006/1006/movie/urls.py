from . import views
from django.urls import path

app_name = "movies" #앱이름

urlpatterns = [
    #movies/ 기본
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
]