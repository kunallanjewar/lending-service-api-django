from rest_framework import serializers
from .models import Profile, Account, Transaction
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
                    username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = get_user_model()
        fields =   ('username',
                    'password',
        )

class ProfileSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Profile
        fields =   ('owner',
                    'first_name',
                    'last_name',
                    'email',
                    'date_created',
                    'date_modified'
        )
        read_only_fields = ('date_created', 'date_modified')

class AccountSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Account
        fields =    ('owner',
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
                    'apr',
                    'account_number',
                    'principal_balance',
                    'interest',
                    'total_amount',
                    'date_created',
                    'date_modified'
        )

class TransactionSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    CHOICES = (('WDW', 'Withdraw'), ('PMT','Payment'))

    owner = serializers.ReadOnlyField(source='owner.username')
    amount = serializers.CharField(required=True)
    account = serializers.CharField(required=True)
    transaction_type = serializers.ChoiceField(choices=CHOICES, required=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Transaction
        fields =    ('owner',
                    'account',
                    'transaction_id',
                    'transaction_type',
                    'amount',
                    'date_created',
                    'date_modified'
        )
        read_only_fields = ('date_created', 'date_modified')
