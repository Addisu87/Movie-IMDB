
from core.genres.models import Genre
from core.genres.serializers import GenreSerializer
from core.abstract.viewsets import AbstractViewSet


class GenreViewSet(AbstractViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
