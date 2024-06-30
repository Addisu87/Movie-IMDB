
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from core.user.serializers import UserSerializer
from core.user.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    http_method_names = ['get', 'patch']
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return User.objects.all()
    #     return User.objects.exclude(is_superuser=True)

    def get_queryset(self):
        return User.objects.all()

    def get_object(self):
        pk = self.kwargs['pk']
        obj = User.objects.get_object_by_public_id(pk)
        self.check_object_permissions(self.request, obj)
        return obj
