from rest_framework import serializers
from .models import User, AccountDetail, Transaction
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(allow_blank=False)

    def create(self,validated_data):
        user = get_user_model().objects.create(
                    username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.email = validated_data['email']
        user.save()
        return user

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = get_user_model()
        fields =   ('username',
                    'password',
                    'first_name',
                    'last_name',
                    'email',
        )

class AccountDetailSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = AccountDetail
        fields =    ('user',
                    'account_number',
                    'credit_line',
                    'apr',
                    'principal_balance',
                    'interest',
                    'total_amount',
                    'date_created',
                    'date_modified'
        )
        read_only_fields = (
                    'account_number',
                    'credit_line',
                    'principal_balance',
                    'interest',
                    'total_amount',
                    'date_created',
                    'date_modified'
        )

class TransactionSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Transaction
        fields =    ('account',
                    'transaction_id',
                    'transaction_type',
                    'amount',
                    'date_created',
                    'date_modified'
        )
        read_only_fields = ('date_created', 'date_modified')
