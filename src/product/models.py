"""
Product Models
"""
from decimal import Decimal

from django.db import models

from django.contrib.postgres.fields import HStoreField

from django.utils.translation import ugettext as _
from django.core.validators import MinValueValidator
from category.models import Category


class Product(models.Model):

    """
    Product Model
    """
    CONDITION_NEW = 'new'
    CONDITION_REFURBISHED = 'refurbished'
    CONDITION_CHOICES = (
        (CONDITION_NEW, _('New')),
        (CONDITION_REFURBISHED, _('Refurbished'))
    )

    sku_number = models.CharField(max_length=255, unique=True, db_index=True)
    brand = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255, db_index=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    price = models.DecimalField(
        max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0'))])
    description = models.TextField()
    attributes = HStoreField(default={})
    parent = models.ForeignKey(
        'self', related_name="variants", null=True, blank=True)
