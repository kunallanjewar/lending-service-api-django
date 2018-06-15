from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields =   ('first_name',
                    'last_name',
                    'email',
                    'date_created',
                    'date_modified'
                    )
        read_only_fields = ('date_created', 'date_modified')

class AccountDetailsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = AccountDetails
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
                    #'credit_line',
                    #'principal_balance',
                    #'interest',
                    #'total_amount',
                    'date_created',
                    'date_modified')

class TransactionsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Transactions
        fields =    ('account',
                    'transaction_id',
                    'transaction_type',
                    'amount',
                    'date_created',
                    'date_modified'
                    )
        read_only_fields = ('date_created', 'date_modified')
