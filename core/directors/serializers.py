from rest_framework import serializers
from core.abstract.serializers import AbstractSerializer
from core.directors.models import Director


class DirectorSerializer(AbstractSerializer):
    birth_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'birth_date',
                  'director_photo', 'nationality', 'created', 'updated']
