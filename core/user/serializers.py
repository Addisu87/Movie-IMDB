from django.conf import settings
from django.contrib.auth import (
    get_user_model
)

from core.abstract.serializers import AbstractSerializer


class UserSerializer(AbstractSerializer):
    """
    Serializer for the user object.
    """

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if not rep['avatar']:
            rep['avatar'] = settings.DEFAULT_AVATAR_URL
            return rep

        if settings.DEBUG:  # debug enabled for dev
            request = self.context.get('request')
            rep['avatar'] = request.build_absolute_uri(rep['avatar'])
        return rep

    class Meta:
        model = get_user_model()
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'username', "name", 'first_name', 'last_name', 'avatar',
                  'email', 'password', 'is_active', 'created', 'updated',]
        # List of all the fields that can only be read by the user
        read_only_fields = ['is_active']
        # password validation
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        """Create and return a User with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        "Update an return user."
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
