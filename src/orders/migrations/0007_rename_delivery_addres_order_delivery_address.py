# Generated by Django 4.0.6 on 2022-08-17 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_delivery_address_order_delivery_addres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_addres',
            new_name='delivery_address',
        ),
    ]
