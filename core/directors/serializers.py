from core.abstract.serializers import AbstractSerializer
from core.directors.models import Director


class DirectorSerializer(AbstractSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'birth_date',
                  'profile_image', 'nationality', 'created', 'updated']
