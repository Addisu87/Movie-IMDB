from rest_framework import serializers
from core.abstract.serializers import AbstractSerializer
from .models import Rating, Review


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class ReviewSerializer(AbstractSerializer):
    class Meta:
        model = Review
        fields = "__all__"
