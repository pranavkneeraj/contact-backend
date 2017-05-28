"""
Product Serializer
"""

from django.db import transaction
from django.conf import settings

from rest_framework import serializers
from category.serializers import CategorySerializer
from category.models import Category
from .models import Product


class CustomDecimalField(serializers.DecimalField):
    """
    User define decimal field error.
    """

    def __init__(self, *a, **k):
        self.default_error_messages[
            'min_value'] = "Input cannot be 0 or negative."
        self.default_error_messages[
            'max_decimal_places'] = "Enter no more than 2 decimal places."
        super().__init__(*a, **k)


class ProductSerializer(serializers.ModelSerializer):

    """
    Product Detail Serializer
    """

    class Meta:
        model = Product
        fields = (
            'id', 'sku_number', 'brand',
            'category', 'name', 'condition', 'description',
            'price', 'parent',)
