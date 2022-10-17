from django.shortcuts import render,redirect
from .forms import ArticleForm
from .models import Article
# Create your views here.

def index(request):
    article_index=Article.objects.all()
    context={
        'article_index':article_index
    }
    return render(request, 'articles/index.html',context)

def create(request):
    if request.method == 'POST':
        article_Form = ArticleForm(request.POST,request.FILES)
        if  article_Form.is_valid():
            article_Form.save()
            return redirect('articles:index')
    else:
         article_Form=ArticleForm()
    context={
        'article_Form': article_Form
    }
    return render(request, 'articles/create.html',context)