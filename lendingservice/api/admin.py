from django.contrib import admin
from .models import (
                Profile,
                Account,
                Transaction,
            )

admin.site.register(Account)
admin.site.register(Profile)
admin.site.register(Transaction)
