from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(
        verbose_name="Genre name",
        max_length=30
    )
    description = models.TextField(
        verbose_name="Genre description",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return str(self.pk) + " " + self.name

class Series(models.Model):
    name = models.CharField(
        verbose_name="Series name",
        max_length=50
    )
    description = models.TextField(
        verbose_name="Series description",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return str(self.pk) + " " + self.name

class TheAuthor(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=30
    )
    surname = models.CharField(
        verbose_name="Surname",
        max_length=30
    )
    biography = models.TextField(
        verbose_name="Biography",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return str(self.pk) + " " + self.name

class PublishingHouse(models.Model):
    name = models.CharField(
        verbose_name="Publishing house name",
        max_length=30
    )
    description = models.TextField(
        verbose_name="Publishing house description",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return str(self.pk) + " " + self.name

class Status(models.Model):
    name = models.CharField(
        verbose_name="Status",
        max_length=30
    )
    description = models.TextField(
        verbose_name="Status",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return str(self.pk) + " " + self.name
