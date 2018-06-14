from rest_framework import serializers
from .models import User

class Serializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('id', 'first_name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
