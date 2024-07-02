
from core.abstract.viewsets import AbstractViewSet
from core.awards.models import Award
from core.awards.serializers import AwardSerializer


class AwardViewSet(AbstractViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
