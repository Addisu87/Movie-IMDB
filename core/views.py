from core.movies.models import Movie  # Replace with your actual Movie model
from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def movie(request):
    movies = Movie.objects.all()  # Query your movies here
    context = {
        'movies': movies,
    }
    return render(request, 'movies.html', context)
