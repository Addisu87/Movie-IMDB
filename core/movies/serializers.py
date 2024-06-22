
from rest_framework import serializers
from core.movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'title', 'description']
        # exclude = ['released']
