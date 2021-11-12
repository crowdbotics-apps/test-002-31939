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


class Contents(models.Model):
    "Generated Model"
    quantity = models.SmallIntegerField()
    sales_price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        "cart.Product",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="contents_product",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="contents_user",
    )


# Create your models here.
