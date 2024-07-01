from core.abstract.serializers import AbstractSerializer
from core.actors.models import Actor


class ActorSerializer(AbstractSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'birth_date',
                  'profile_image', 'nationality', 'created', 'updated']
