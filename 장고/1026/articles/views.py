from django.shortcuts import render,redirect
from django.http import JsonResponse
from articles.forms import ArticleForm,CommentForm
from articles.models import Article,Comment

# Create your views here.
def index(request):
    article_index = Article.objects.all()
    context={
        'article_index': article_index
    }
    return render(request, 'articles/index.html',context)
def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
        return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context ={
        'article_form':article_form
    }
    return render(request, 'articles/create.html',context)

def detail(request,articles_pk):
    article = Article.objects.get(pk=articles_pk)
    comment_form = CommentForm()
    comments=article.comment_set.all()
    context={
        'article':article,
        'comment_form':comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html',context)

def comments_create(request,article_pk):
    print(request.POST)
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment =comment_form.save()
    context={
        'content':comment.content,
        'userName':comment.user.username
    }
    return JsonResponse(context)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)