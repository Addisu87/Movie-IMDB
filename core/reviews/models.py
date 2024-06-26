from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.abstract.models import AbstractModel
from core.movies.models import Movie


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10)])
    source = models.CharField(max_length=175)
    movie = models.ForeignKey(
        Movie, related_name='ratings', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Calculate and update average rating for the movie
        self.movie.update_average_rating()

    def __str__(self):
        return f'{self.source}: {self.rating}'


class Review(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=True)
    active = models.BooleanField(default=True)
    movie = models.ForeignKey(
        Movie, related_name='reviews', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'Review by {self.user.username} on {self.movie.title}'
