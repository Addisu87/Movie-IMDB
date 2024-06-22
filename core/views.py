from core.movies.models import Movie  # Replace with your actual Movie model
from django.shortcuts import render


def home(request):
    return render(request, 'core/content.html')

# views.py


def movie_list(request):
    movies = Movie.objects.all()  # Query your movies here
    context = {
        'movies': movies,
    }
    return render(request, 'movies.html', context)
