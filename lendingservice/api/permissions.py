from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsOwner(BasePermission):
    """ Only allow users to edit their information."""

    def has_object_permission(self, request, view, obj):
        """ Return True if permission is granted."""
        if isinstance(obj, User):
            print(request.user)
            return obj.username == request.user
        return obj.username == request.user
