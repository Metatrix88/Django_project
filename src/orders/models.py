from django.db import models
from django.contrib.auth import get_user_model
from card_product import models as cp_models
# Create your models here.

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='carts',
        verbose_name='Customer',
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
        auto_now=False
    )
    updated_date = models.DateTimeField(
        verbose_name='Updated',
        auto_now_add=False,
        auto_now=True
    )

    def total_price(self):
        total = 0
        for good in self.goods.all():
            total +=good.price
        return total


class BookInCart(models.Model):
    cart = models.ForeignKey(
        'orders.Cart',
        on_delete=models.PROTECT,
        related_name='goods',
        verbose_name='Cart'
    )
    book = models.ForeignKey(
        cp_models.Book,
        on_delete=models.PROTECT,
        related_name='goods',
        verbose_name='Book'
    )
    quantity = models.SmallIntegerField(
        verbose_name='Quantity'
    )
    price = models.DecimalField(
        verbose_name='Price',
        decimal_places=2,
        max_digits=5,
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
        auto_now=False
    )
    updated_date = models.DateTimeField(
        verbose_name='Updated',
        auto_now_add=False,
        auto_now=True
    )

class Order(models.Model):
    cart = models.ForeignKey(
        'orders.Cart',
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name='Cart'
    )
    name_and_surname = models.CharField(
        verbose_name="Name and surname of the recipient",
        blank=True,
        null=True,
        max_length=60
    )
    phone = models.IntegerField(
        verbose_name="Phone",
        blank=True,
        null=True
    )
    delivery_address = models.TextField(
        verbose_name="Delivery address",
        blank=True,
        null=True
    )
    additional_information = models.TextField(
        verbose_name="Additional Information",
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
        auto_now=False
    )
    updated_date = models.DateTimeField(
        verbose_name='Updated',
        auto_now_add=False,
        auto_now=True
    )
