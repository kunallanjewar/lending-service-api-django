# Generated by Django 2.0.6 on 2018-06-15 06:50

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180615_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdetails',
            name='interest',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=2),
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AddField(
            model_name='transactions',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
