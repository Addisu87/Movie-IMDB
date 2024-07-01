from core.abstract.serializers import AbstractSerializer
from core.languages.models import Language


class LanguageSerializer(AbstractSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language', 'created', 'updated']
