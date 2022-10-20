
from django.shortcuts import render,redirect
from .forms import ArticleForm,CommentForm
# from django.contrib.auth.decorators import login_required
# Create your views here.

def create(request):
    if request.method == "POST":
        article_Form=ArticleForm(request.POST, request.FILES)
        if article_Form.is_valid():
            article_Form.save()
            return redirect('articles:index')
    else:
        article_Form=ArticleForm()
    context={
        'article_Form':article_Form
    }
    return render(request, 'articles/create.html',context)

def index(request):
    return render(request, "articles/index.html")