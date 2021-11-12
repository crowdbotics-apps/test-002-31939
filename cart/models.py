from django.conf import settings
from django.db import models


class Product(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=200,
    )
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    description = models.TextField()
    sku = models.CharField(
        max_length=256,
    )


class Content(models.Model):
    "Generated Model"
    quantity = models.SmallIntegerField()
    sales_price = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
    )
    product = models.ForeignKey(
        "cart.Product",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="contents_product",
    )
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="contents_user",
    )


# Create your models here.
