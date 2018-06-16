from django.db import models
import uuid
from decimal import Decimal

class User(models.Model):
    username = models.ForeignKey(
                'auth.User',
                related_name='owner',
                on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=254, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.email)

class AccountDetail(models.Model):
    user = models.ForeignKey(
                'User',
                on_delete=models.CASCADE,
                default=None
    )
    account_number = models.UUIDField(
                primary_key=True,
                default=uuid.uuid4,
                editable=False
    )
    credit_line = models.DecimalField(
                max_digits=50,
                decimal_places=2,
                default=Decimal('0.00')
    )
    principal_balance = models.DecimalField(
                max_digits=50,
                decimal_places=2,
                default=Decimal('0.00')
    )
    apr = models.DecimalField(
                max_digits=5,
                decimal_places=2,
                default=Decimal('0.00')
    )

    interest = models.DecimalField(
                max_digits=10,
                decimal_places=2,
                default=Decimal('0.00')
    )
    total_amount = models.DecimalField(
                max_digits=50,
                decimal_places=2,
                default=Decimal('0.00')
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.account_number)

class Transaction(models.Model):
    account = models.ForeignKey(
                'AccountDetail',
                on_delete=models.CASCADE,
                default = None
    )
    transaction_id = models.UUIDField(
                primary_key=True,
                default=uuid.uuid4,
                editable=False
    )
    amount = models.DecimalField(
                max_digits=10,
                decimal_places=2,
                default=Decimal('0.00')
    )
    CHOICES = (('WDW', 'Withdraw'), ('PMT','Payment'))
    transaction_type = models.CharField(max_length=3, choices=CHOICES)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.transaction_id)
