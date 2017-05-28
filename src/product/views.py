"""
Product Views
"""

from django.conf import settings
from django import forms

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import filters

from utils.filters import SimpleProductArrayFilter
# from django_countries import countries
from utils.viewsets import PaginatedViewSetMixin

from .models import Product
from .serializers import ProductSerializer
from .permissions import AdminWriteOnly


class ProductFilter(filters.FilterSet):
    """
    Filter a product using SKU.
    """
    sku_number = SimpleProductArrayFilter(base_field=forms.CharField())

    class Meta:
        model = Product
        fields = ['sku_number', 'name', 'brand']


class ProductViewSet(PaginatedViewSetMixin):  # pylint: disable=too-many-ancestors
    """
    Viewset for Product Details
    """
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    queryset = Product.objects.all()
    permission_classes = (AdminWriteOnly, )
