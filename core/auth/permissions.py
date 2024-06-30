from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Object-level permission to only allow owners of an object to edit it.
        """

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests
        if request.method in SAFE_METHODS:
            return True

        # Check if the user is anonymous
        if request.user.is_anonymous:
            return False

        # Write permissions are only allowed to the owner of the object
        return request.user.id == obj.id

    def has_permission(self, request, view):
        """Global permission check for crud operations."""
        if view.basename in ['user', 'auth-logout']:
            # Allow read-only methods for anonymous users
            if request.method in SAFE_METHODS:
                return True

            # Check if the user is authenticated
            return request.user.is_authenticated
        return False
