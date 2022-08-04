from django.db import models
from datetime import datetime

class Book(models.Model):
    name = models.CharField(
        verbose_name="Book name",
        max_length=50
    )
    image = models.ImageField(
        verbose_name="Image book",
        upload_to='uploads/%Y/%m/%d/',
        blank=True,
        null=True
    )
    price = models.IntegerField(
        verbose_name="Price book (byn)",
        blank=True,
        null=True
    )
    author = models.ManyToManyField(
        'catalogue.TheAuthor',
        verbose_name='Author',
        related_name='books'
    )
    series = models.ForeignKey(
        'catalogue.Series',
        on_delete=models.PROTECT,
        verbose_name='Series',
        related_name='books'
    )
    genre = models.ManyToManyField(
        'catalogue.Genre',
        verbose_name='Genre',
        related_name='books'
    )
    the_year_of_publishing = models.IntegerField(
        verbose_name="The year of publishing",
        blank=True,
        null=True
    )
    pages = models.IntegerField(
        verbose_name="Pages",
        blank=True,
        null=True
    )
    binding = models.CharField(
        verbose_name="Binding",
        max_length=30,
        blank=True,
        null=True
    )
    format = models.CharField(
        verbose_name="Format",
        max_length=30,
        blank=True,
        null=True
    )
    isbn = models.IntegerField(
        verbose_name="ISBN",
        blank=True,
        null=True
    )
    weight = models.IntegerField(
        verbose_name="Weight (gram)",
        blank=True,
        null=True
    )
    age_restrictions = models.IntegerField(
        verbose_name="Age restrictions",
        blank=True,
        null=True
    )
    publishing_house = models.ForeignKey(
        'catalogue.PublishingHouse',
        on_delete=models.PROTECT,
        verbose_name='PublishingHouse',
        related_name='books'
    )
    quantity = models.IntegerField(
        verbose_name="Quantity",
        blank=True,
        null=True
    )
    active = models.BooleanField(
        verbose_name="Are available (yes/no)",
        blank=True,
        null=True
    )
    rating = models.IntegerField(
        verbose_name="Rating",
        blank=True,
        null=True
    )
    data_register = models.DateField(
        editable=True,
        verbose_name="Date of entry into the catalog",
        auto_now_add=True
    )
    data_changes = models.DateField(
        editable=True,
        verbose_name="Date of the last change of the card",
        auto_now=True

    )
    def __str__(self):
        return self.name
