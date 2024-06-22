import uuid
import os


from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator


def movie_image_file_path(instance, filename):
    """
    Generate file path for new movie image.
    """
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('media', 'movie', filename)


# class Rating(models.Model):
#     rating = models.FloatField(
#         validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
#     source = models.CharField(max_length=175)

# This is a many-to-many relationship: a movie belongs to
# one rating and a rating contains multiple movies


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    slug = models.SlugField(max_length=150, unique=True)
    Plot = models.TextField(max_length=300, blank=True)
    released_year = models.DateField()
    movie_length = models.IntegerField()
    poster = models.ImageField(blank=True, upload_to=movie_image_file_path)
    # rating = models.ManyToManyField(Rating, related_name='rating', blank=True)

    def __str__(self):
        return self.title
