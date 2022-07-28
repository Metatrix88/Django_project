# Generated by Django 4.0.6 on 2022-07-27 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_product', '0004_alter_book_data_changes_alter_book_data_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='data_changes',
            field=models.DateField(default=datetime.date.today, verbose_name='Date of the last change of the card'),
        ),
        migrations.AlterField(
            model_name='book',
            name='data_register',
            field=models.DateField(default=datetime.date.today, verbose_name='Date of entry into the catalog'),
        ),
    ]