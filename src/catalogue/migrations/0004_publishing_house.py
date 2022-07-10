# Generated by Django 4.0.6 on 2022-07-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_the_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publishing_house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Publishing house name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Publishing house description')),
            ],
        ),
    ]
