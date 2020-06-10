from django.shortcuts import render

# Create your views here.


def index_views(request):
    return render(request, 'testapp/index.html')


def movies_views(request):

    movies = 'Ek Tha Tiger'

    my_movies = {
        'movie': movies
    }

    return render(request, 'testapp/movies.html', my_movies)


def politics_views(request):
    return render(request, 'testapp/politics.html')


def sports_views(request):
    return render(request, 'testapp/sports.html')
