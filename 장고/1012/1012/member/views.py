from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from member.models import User
from .forms import CustomUserCreationFrom#회원가입 form
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm#로그인 form
from django.contrib.auth.decorators import login_required
# Create your views here.


def main(request):

    return render(request, 'accounts/main.html')

def create(request):#회원가입
    if request.method == "POST":
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:main')
    else:
        form =CustomUserCreationFrom()
    context ={
        'form':form
    }
    return render(request, 'accounts/create.html',context)
@login_required
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'accounts/index.html', context)
@login_required
def detail(request,pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user':user
    }
    return render(request, 'accounts/detail.html',context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm()#modelform이 아님
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or 'accounts:detail') 
    else:
        form =AuthenticationForm()
    context ={
        'form':form
    }
    return render(request, 'accounts/login.html',context)