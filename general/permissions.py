from rest_framework import permissions
from django.conf import settings


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to add and edit info.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return True
