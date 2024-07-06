
from rest_framework import viewsets

from core.movies.models import Movie
from core.movies.serializers import MovieSerializer


# ViewSets define the view behavior.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
