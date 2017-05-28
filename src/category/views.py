"""
Category Views
"""
import django_filters

from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from product.models import Product
from product.permissions import AdminWriteOnly
from product.serializers import ProductSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class CategoryFilter(django_filters.FilterSet):
    """
    Category Filter.
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name', ]


class CategoryViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Viewset for Category Details
    """
    permission_classes = (AdminWriteOnly, )
    filter_class = CategoryFilter
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    @detail_route(url_path="products")
    def get_products(self, request, pk):
        products = ProductSerializer(
            list(Product.objects.filter(category=pk)), many=True)

        return Response(products.data)

    @detail_route(url_path="sub-category")
    def get_products(self, request, pk):
        print(pk)
        self.queryset = self.get_queryset().filter(parent=pk)
        return Response(CategorySerializer(list(self.queryset), many=True).data)
