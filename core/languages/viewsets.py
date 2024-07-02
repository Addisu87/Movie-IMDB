from core.abstract.viewsets import AbstractViewSet
from core.languages.models import Language
from core.languages.serializers import LanguageSerializer


class LanguageViewSet(AbstractViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
