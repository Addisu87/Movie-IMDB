
from core.awards.models import Award

from core.abstract.serializers import AbstractSerializer


class AwardSerializer(AbstractSerializer):
    class Meta:
        model = Award
        fields = ['id', 'award_name', 'created', 'updated']
