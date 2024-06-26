
from rest_framework import serializers
from .models import Movie

from core.abstract.serializers import AbstractSerializer
from core.reviews.serializers import ReviewSerializer


class MovieSerializer(AbstractSerializer):
    # Nested serializer for reviews
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
