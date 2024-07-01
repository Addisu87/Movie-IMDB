
from core.cinemas.models import Cinema
from core.abstract.serializers import AbstractSerializer


class CinemaSerializer(AbstractSerializer):
    class Meta:
        model = Cinema
        fields = ['id', 'cinema_name', 'city', 'state',
                  'country', 'street_number',  'created', 'updated']
