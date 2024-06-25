import uuid
import os

from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def movie_image_file_path(instance, filename):
    """
    Generate file path for new movie image.
    """
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('movie', filename)


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    slug = models.SlugField(max_length=150, unique=True, default='')
    plot = models.TextField(max_length=300, blank=True, default='')
    poster = models.ImageField(blank=True, upload_to=movie_image_file_path)
    released_year = models.DateField()
    movie_length = models.IntegerField()

    class Meta:
        ordering = ['-released_year']

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(10.0)]
    )
    source = models.CharField(max_length=175)

    def __str__(self):
        return f'{self.source}: {self.rating}'


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(
        Movie, related_name='reviews', on_delete=models.CASCADE)
    rating = models.ForeignKey(
        Rating, related_name='reviews', on_delete=models.CASCADE, default=1.0)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'Review by {self.user.username} on {self.movie.title}'
