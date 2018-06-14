from django.db import models
import uuid

class User(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.first_name)

class AccountDetails(models.Model):
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
                max_digits=5,
                decimal_places=2,
                null=True,
                blank=True
            )
    principal_balance = models.DecimalField(
                max_digits=5,
                decimal_places=2,
                null=True,
                blank=True
            )
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)

class Transactions(models.Model):
    account = models.ForeignKey(
                'AccountDetails',
                on_delete=models.CASCADE,
                default = None
            )
    transaction_id = models.UUIDField(
                primary_key=True,
                default=uuid.uuid4,
                editable=False
            )
    transaction_type = models.CharField(max_length=10, null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
