from core.abstract.serializers import AbstractSerializer
from core.awards.models import Award


class AwardSerializer(AbstractSerializer):
    class Meta:
        model = Award
        fields = ['id', 'award_name', 'created', 'updated']
