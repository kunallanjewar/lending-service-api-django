from rest_framework.permissions import BasePermission
from .models import User as UserModel, AccountDetail, Transaction

class IsOwner(BasePermission):
    """ Only allow users to edit their information."""

    def has_permission(self, request, view, data):
        """ Return True if permission is granted."""
        if is_instance(data, UserModel):
            return data.owner == request.user
        return data.owner == request.user
