
from django.db import models

from core.movies.models import Movie
from core.abstract.models import AbstractModel


class Language(AbstractModel):
    movie = models.ForeignKey(
        Movie, related_name='language', on_delete=models.CASCADE)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.language}"
