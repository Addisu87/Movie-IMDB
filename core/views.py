from core.movies.models import Movie  # Replace with your actual Movie model
from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')
