# Generated by Django 5.2.1 on 2025-06-07 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
