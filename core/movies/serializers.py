
from rest_framework import serializers
from .models import Movie, Review, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    rating = RatingSerializer()

    class Meta:
        model = Review
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
