from core.abstract.viewsets import AbstractViewSet
from core.directors.models import Director
from core.directors.serializers import DirectorSerializer


class DirectorViewSet(AbstractViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get_top_directors(self):
        return self.queryset.all()[:6]
