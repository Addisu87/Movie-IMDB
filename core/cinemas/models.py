from django.db import models

from core.abstract.models import AbstractModel
from core.movies.models import Movie


class Cinema(AbstractModel):
    movie = models.ForeignKey(
        Movie, related_name='cinema', on_delete=models.CASCADE)
    cinema_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    street_number = models.IntegerField()

    def __str__(self):
        return f'{self.cinema_name}, {self.city},{self.country}'
