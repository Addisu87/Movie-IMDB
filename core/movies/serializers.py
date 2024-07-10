
from rest_framework import serializers
from .models import Movie

from core.abstract.serializers import AbstractSerializer
from core.actors.serializers import ActorSerializer
from core.directors.serializers import DirectorSerializer
from core.reviews.serializers import ReviewSerializer
from core.reviews.serializers import RatingSerializer


class MovieSerializer(AbstractSerializer):
    # Nested serializer for reviews
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    average_rating = serializers.ReadOnlyField()

    # user = serializers.StringRelatedField(read_only=True)
    # rating = RatingSerializer(read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'slug', 'plot', 'poster', 'released_year',
            'duration', 'actors', 'directors', 'average_rating',
            'created_at', 'updated_at'
        ]
