# Generated by Django 2.0.6 on 2018-06-15 04:56

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180615_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetails',
            name='credit_line',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='principal_balance',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5),
        ),
    ]
