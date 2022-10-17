from . import views
from django.urls import path

app_name='articles'
urlpatterns = [
    #articles
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]