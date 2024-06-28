
from django.shortcuts import render
from core.movies.models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'core/content.html', {'movies': movies})
