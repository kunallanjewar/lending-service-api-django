from rest_framework import serializers
from .models import User, AccountDetail, Transaction

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields =   ('first_name',
                    'last_name',
                    'email',
                    'username',
                    'date_created',
                    'date_modified'
        )
        read_only_fields = ('username','date_created', 'date_modified')

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
                    #'credit_line',
                    #'principal_balance',
                    #'interest',
                    #'total_amount',
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
