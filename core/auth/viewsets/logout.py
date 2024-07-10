from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError


class LogoutViewSet(viewsets.ViewSet):
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        refresh = request.data.get('refresh')

        if refresh is None:
            raise ValidationError({'detail': 'Refresh token is required'})

        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({'detail': 'Successfully logged out'}, status=status.HTTP_204_NO_CONTENT)
        except TokenError:
            raise ValidationError({'detail': 'The refresh token is invalid'})
