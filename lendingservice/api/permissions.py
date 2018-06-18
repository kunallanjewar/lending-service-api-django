from rest_framework.permissions import BasePermission
from .models import Profile, Account, Transaction

class IsProfileOwner(BasePermission):
    """ Only allow users to edit their information."""
    def has_object_permission(self, request, view, obj):
        """ Return True if permission is granted."""
        if isinstance(obj, Profile):
            return obj.owner == request.user
        return False

class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """ Return True if permission is granted."""
        if isinstance(obj, Account):
            return obj.owner == request.user
        return False

class IsTransactionOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """ Return True if permission is granted."""
        if isinstance(obj, Transaction):
            return obj.owner == request.user
        return False
