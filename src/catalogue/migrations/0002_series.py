# Generated by Django 4.0.6 on 2022-07-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Series name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Series description')),
            ],
        ),
    ]