import uuid
import os

from django.conf import settings
from django.db import models


def movie_image_file_path(instance, filename):
    """
    Generate file path for new movie image.
    """
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('media', 'movie', filename)


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    slug = models.SlugField(max_length=150, unique=True, default='')
    Plot = models.TextField(max_length=300, blank=True, default='')
    poster = models.ImageField(blank=True, upload_to=movie_image_file_path)
    released_year = models.DateField()
    movie_length = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-released_year']


class Review(models.Model):
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(
        Movie, related_name='movie_review', on_delete=models.CASCADE)
