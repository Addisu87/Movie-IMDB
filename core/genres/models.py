from django.db import models
from core.abstract.models import AbstractModel


class Genre(AbstractModel):
    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.genre_name}"
