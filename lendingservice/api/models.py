from django.db import models
from decimal import Decimal
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
import uuid

'''
class User(models.Model):
    owner = models.ForeignKey(
                'auth.User',
                related_name='users',
                on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=254, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.owner)
'''
class AccountDetail(models.Model):
    owner = models.ForeignKey(
                'auth.User',
                related_name='users',
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
    '''owner = models.ForeignKey(
                'auth.User',
                related_name='owner',
                on_delete=models.CASCADE,
                default=None
    )
    account = models.ForeignKey(
                'AccountDetail',
                on_delete=models.CASCADE,
                default = None
    )'''
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

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
