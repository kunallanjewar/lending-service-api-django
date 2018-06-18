from rest_framework.permissions import BasePermission
from .models import User as Profile, Account, Transaction
from django.contrib.auth.models import User

class IsProfileOwner(BasePermission):
    """ Only allow users to edit their information."""

    def has_object_permission(self, request, view, obj):
        """ Return True if permission is granted."""
        if isinstance(obj, Profile):
            return obj.owner == request.user
        return False#return obj.owner == request.user

class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """ Return True if permission is granted."""
        if isinstance(obj, Account):
            return obj.owner == request.user
        return False#obj.owner == request.user

class IsTransactionOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """ Return True if permission is granted."""
        if isinstance(obj, Transaction):
            return obj.owner == request.user
        return False#obj.owner == request.user
