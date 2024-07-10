from rest_framework_simplejwt.tokens import (
    RefreshToken, TokenError
)
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


class LogoutViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        refresh = request.data.get('refresh')

        if refresh is None:
            raise ValidationError({'detail': 'Refresh token is required'})

        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response({'detail': 'Successfully logged out'}, status=status.HTTP_204_NO_CONTENT)
        except TokenError:
            raise ValidationError({'detail': 'The refresh token is invalid'})
