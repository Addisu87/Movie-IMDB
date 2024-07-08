from core.abstract.viewsets import AbstractViewSet
from core.actors.models import Actor
from core.actors.serializers import ActorSerializer


class ActorViewSet(AbstractViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_queryset(self):
        return Actor.objects.all()

    def get_top_actors(self):
        return self.queryset.all()[:12]
