from rest_framework import serializers
from core.abstract.serializers import AbstractSerializer
from .models import Rating, Review


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['rating', 'source', 'movie', 'user']


class ReviewSerializer(AbstractSerializer):

    class Meta:
        model = Review
        fields = [
            'id', 'content', 'active',
            'created_at', 'updated_at'
        ]
