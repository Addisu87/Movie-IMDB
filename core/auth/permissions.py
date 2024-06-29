from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Object-level permission to only allow owners
            of an object to edit it.
        """
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests
        if view.basename in ['user']:
            if request.method in SAFE_METHODS:
                return True
            # Write permissions are only allowed to the owner of the reviews
            return bool(request.user.id == obj.id)
        return False

    def has_permission(self, request, view):
        """Global permission check for crud operations."""
        if view.basename in ['user', 'auth-logout']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            return bool(request.user and request.user.is_authenticated)
        return False
