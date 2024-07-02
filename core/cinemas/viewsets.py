from core.abstract.viewsets import AbstractViewSet
from core.cinemas.models import Cinema
from core.cinemas.serializers import CinemaSerializer


class CinemaViewSet(AbstractViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
