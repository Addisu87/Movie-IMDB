
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.user.serializers import UserSerializer
from core.user.models import User


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
