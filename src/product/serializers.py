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

    # def __init__(self, *a, **k):
    #     if a[0:
    #         self.fields['category'] = CategorySerializer()
    #     return super().__init__(*a, **k)

    class Meta:
        model = Product
        fields = (
            'id', 'sku_number', 'brand',
            'category', 'name', 'condition', 'description',
            'price', 'parent',)

    # @transaction.atomic
    # def create(self, data):
    #     product_details = data
    #     price_details = product_details['price_details']
    #     shipping_details = product_details['shipping_details']
    #     del product_details['price_details'], product_details[
    #         'shipping_details']
    #     product = Product.objects.create(**product_details)
    #     price_details['product'] = product
    #     shipping_details['product'] = product
    #     data['price_details'] = PriceDetail.objects.create(**price_details)
    #     data['shipping_details'] = ShippingDetail.objects.create(
    #         **shipping_details)
    #     data['id'] = product.id
    #     data['parent'] = product.parent
    #     return data

    # @transaction.atomic
    # def update(self, instance, data):
    #     product_details = data
    #     price_details = product_details['price_details']
    #     shipping_details = product_details['shipping_details']
    #     del product_details[
    #         'price_details'], product_details['shipping_details']
    #     product_details['category'] = Category.objects.get(
    #         name=data['category']['name'].split('>')[-1].strip(),
    #         parent_id=data['category']['parent'].id if data[
    #             'category']['parent'] else None
    #     )
    #     product = Product.objects.filter(
    #         id=instance.id)
    #     product.update(**product_details)
    #     PriceDetail.objects.filter(
    #         id=instance.price_details.id).update(**price_details)
    #     ShippingDetail.objects.filter(
    #         id=instance.shipping_details.id).update(**shipping_details)
    #     return product[0]
