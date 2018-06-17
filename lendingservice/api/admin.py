from django.contrib import admin
from .models import (
                AccountDetail,
                Transaction,
            )

admin.site.register(AccountDetail)
admin.site.register(Transaction)
