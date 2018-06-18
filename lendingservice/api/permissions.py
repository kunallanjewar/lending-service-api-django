from rest_framework.permissions import BasePermission
from .models import User as UserModel, AccountDetail, Transaction
from django.contrib.auth.models import User

class IsOwner(BasePermission):
    """ Only allow users to edit their information."""

    def has_object_permission(self, request, view, obj):
        """ Return True if permission is granted."""
        if isinstance(obj, UserModel):
            return obj.owner == request.user
        return obj.owner == request.user

class IsUserHimself(BasePermission):
    def has_object_permission(self, request, view, obj):
        """ Return True if permission is granted."""
        if isinstance(obj, User):
            return obj.username == request.user
        return obj.username == request.user
