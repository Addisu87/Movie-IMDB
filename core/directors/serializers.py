
from core.directors.models import Director
from core.abstract.serializers import AbstractSerializer


class DirectorSerializer(AbstractSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'birth_date',
                  'profile_image', 'nationality',  'created', 'updated']
