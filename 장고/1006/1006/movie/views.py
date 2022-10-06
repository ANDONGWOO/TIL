from django.shortcuts import render,redirect
from movie.models import Movie
from .forms import MovieFrom
# Create your views here.
def index(request):
    movie = Movie.objects.order_by('-pk')
    context={
        'movies':movie
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        Movie_From = MovieFrom(request.POST)#인스턴스화
        if Movie_From .is_valid():
            Movie_From .save()
            return redirect('movies:index')
    else:
        Movie_From = MovieFrom()

    context={
        'Movie_From': Movie_From
    }
    return render(request, 'movies/create.html' , context=context)


    
    