from rest_framework import serializers
from core.abstract.serializers import AbstractSerializer
from core.actors.models import Actor


class ActorSerializer(AbstractSerializer):
    birth_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'birth_date',
                  'profile_image', 'nationality', 'created', 'updated']
