# Generated by Django 4.0.6 on 2022-08-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_product', '0009_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Price book (byn)'),
        ),
    ]
