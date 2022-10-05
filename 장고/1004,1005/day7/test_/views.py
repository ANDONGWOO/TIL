from urllib import request
from django.shortcuts import render,redirect
from test_.models import Test
from .forms import TestFrom
# Create your views here.

def index(request):
    articles = Test.objects.order_by('-pk')
    context={
        'articles':articles
    }
    return render(request, 'test_/index.html' , context)

def create(request):
    if request.method == 'POST':
        test_from = TestFrom(request.POST)
        if test_from.is_valid():
            test_from.save()
            return redirect('day7:index')
    else:
        test_from = TestFrom()

    context={
        'test_from': test_from
    }
    return render(request, 'test_/new.html' , context=context)

def detail(request, pk):
    article = Test.objects.get(pk=pk)
    context={
        'article':article
    }
    return render(request, 'test_/detail.html', context)

def update(request, pk):
    article = Test.objects.get(pk=pk)
    if request.method == 'POST':
        test_from = TestFrom(request.POST,instance=article)#인스턴스화
        if test_from.is_valid():
            test_from.save()
            return redirect('day7:detail', article.pk)
    else:
        test_from = TestFrom( instance=article)
    context={
        'test_from' : test_from
    }
    return render(request, 'test_/update.html', context)
