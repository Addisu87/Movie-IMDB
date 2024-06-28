import os
import uuid
from django.conf import settings
from django.db import models
from core.abstract.models import AbstractModel


def movie_image_file_path(instance, filename):
    """
    Generate file path for new movie image.
    """
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join('movie', filename)


class Movie(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(max_length=150, unique=True, default="")
    plot = models.TextField(max_length=300, default="")
    poster = models.ImageField(blank=True, upload_to=movie_image_file_path)
    released_year = models.DateField()
    duration = models.IntegerField()

    class Meta:
        ordering = ['-released_year']

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        # Calculate average rating for the movie
        ratings = self.ratings.all()
        if ratings.exists():
            avg_rating = sum(
                rating.rating for rating in ratings) / ratings.count()
            return avg_rating
        else:
            return 1.0
