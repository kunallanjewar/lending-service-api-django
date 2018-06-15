from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('first_name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class AccountDetailsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = AccountDetails
        fields = ('first_name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class TransactionsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Transactions
        fields = ('first_name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
