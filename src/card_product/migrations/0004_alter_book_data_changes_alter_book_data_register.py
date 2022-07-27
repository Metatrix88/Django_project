# Generated by Django 4.0.6 on 2022-07-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_product', '0003_alter_book_active_alter_book_data_changes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='data_changes',
            field=models.DateField(auto_now=True, verbose_name='Date of the last change of the card'),
        ),
        migrations.AlterField(
            model_name='book',
            name='data_register',
            field=models.DateField(auto_now_add=True, verbose_name='Date of entry into the catalog'),
        ),
    ]
