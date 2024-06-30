
from django.db import models

from core.movies.models import Movie


class Genre(models.Model):
    movie = models.ForeignKey(
        Movie, related_name='genre', on_delete=models.CASCADE)
    genre_name = models.CharField(max_length=50)
