from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationFrom,CustomUserChangeFrom #회원가입/수정
from member.models import User
from django.contrib.auth.forms import AuthenticationForm#로그인
from django.contrib.auth import login as auth_login#로그인
from django.contrib.auth import logout as auth_logout#로그아웃
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def main(request):
    return render(request, 'accounts/main.html')

def create(request):#회원가입
    if request.method == "POST":
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('member:main')
    else:
        form =CustomUserCreationFrom()
    context ={
        'form':form
    }
    return render(request, 'accounts/create.html',context)

def index(request):#회원목록
    user_index = User.objects.all()
    context={
        'user_index':user_index
    }
    return render(request, 'accounts/index.html',context)
@login_required
def detail(request,pk):
    
    user_detail = get_user_model().objects.get( pk=pk)
    context={
        'user_detail':user_detail
    }
    return render(request, 'accounts/detail.html',context)
    

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'member:main')
    else:
        form = AuthenticationForm()
    context={
        'form':form
    }
    return render(request, 'accounts/login.html',context)
def logout(request):
    auth_logout(request)
    return redirect( 'member:create')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeFrom(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('member:main', request.user.pk)
    else:
        form = CustomUserChangeFrom(instance=request.user)
    context={
        'form':form
    }
    return render(request, 'accounts/update.html',context)

