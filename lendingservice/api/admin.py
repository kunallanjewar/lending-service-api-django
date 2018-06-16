from django.contrib import admin
from .models import (
                User,
                AccountDetails,
                Transactions
            )

admin.site.register(User)
admin.site.register(AccountDetails)
admin.site.register(Transactions)
