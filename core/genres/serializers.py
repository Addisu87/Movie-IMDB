from core.genres.models import Genre
from core.abstract.serializers import AbstractSerializer


class GenreSerializer(AbstractSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_name', 'created', 'updated']
