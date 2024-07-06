
import datetime
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q
from .models import Movie
from .serializers import MovieSerializer


# ViewSets define the view behavior.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # def get_queryset(self):
    #     return Movie.objects.all()

    # def get_similar_movies(self, movie_id):
    #     try:
    #         movie = Movie.objects.get(pk=movie_id)
    #     except Movie.DoesNotExist:
    #         return []

    #     similar_movies = self.queryset.filter(
    #         ~Q(pk=movie.pk),  # Exclude the current movie itself
    #         genres__in=movie.genres.all()  # Filter by shared genres
    #     ).distinct()[:4]

    #     return similar_movies

    def get_popular_movies(self):
        return Movie.objects.filter(
            ratings__gte=7.5
        ).order_by('-ratings')[:4]

    def get_upcoming_movies(self):
        today = datetime.date.today()
        return Movie.objects.filter(
            released_year__gte=today
        ).order_by('released_year')[:4]

    # def get_favorite_movies(self):
    #     favorite_movies = self.queryset.filter(
    #         is_favorite=True).order_by('-released_year')[:4]
    #     return favorite_movies
