from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationFrom
from django.contrib.auth import get_user_model
# Create your views here.

def main(request):
    return render(request, 'signup/main.html')

def index(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'users': user
    }
    return render(request, 'signup/index.html', context)

def detail(request ,user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context ={
        'user':user
    }
    return render(request, 'signup/detail.html',context)

def create(request):
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup:main')
    else:
        form = CustomUserCreationFrom()
    context={
        'form':form
    }
    return render(request, 'signup/cerate.html', context)