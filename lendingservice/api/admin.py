from django.contrib import admin
from .models import (
                User,
                AccountDetail,
                Transaction,
            )

admin.site.register(User)
admin.site.register(AccountDetail)
admin.site.register(Transaction)
