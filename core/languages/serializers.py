
from core.languages.models import Language
from core.abstract.serializers import AbstractSerializer


class LanguageSerializer(AbstractSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language', 'created', 'updated']
