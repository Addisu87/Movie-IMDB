

from .models import Movie

from core.abstract.serializers import AbstractSerializer
from core.reviews.serializers import ReviewSerializer
from core.reviews.serializers import RatingSerializer


class MovieSerializer(AbstractSerializer):
    # Nested serializer for reviews
    # user = serializers.StringRelatedField(read_only=True)
    # rating = RatingSerializer(read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'slug', 'plot', 'poster',
                  'released_year', 'duration', 'actors', 'directors',
                  'genres', 'created', 'updated']
