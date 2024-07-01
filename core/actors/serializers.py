
from core.actors.models import Actor
from core.abstract.serializers import AbstractSerializer


class ActorSerializer(AbstractSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'birth_date',
                  'profile_image', 'nationality',  'created', 'updated']
