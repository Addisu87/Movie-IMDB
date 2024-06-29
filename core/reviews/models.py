from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.abstract.models import AbstractModel
from core.movies.models import Movie


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='rating', on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie, related_name='ratings', on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(10)])
    source = models.CharField(max_length=175)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

       # Update average rating for the movie after saving a new rating
        self.movie.save()

    def __str__(self):
        return f'{self.source}: {self.rating}'


class Review(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='reviews', on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'Review by {self.user.username} on {self.movie.title}'
