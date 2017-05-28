"""
Category Views
"""
import django_filters

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_extensions.mixins import NestedViewSetMixin


from .models import Category
from .serializers import CategorySerializer
from product.permissions import AdminWriteOnly


class CategoryFilter(django_filters.FilterSet):
    """
    Category Filter.
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name', ]


class CategoryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Viewset for Category Details
    """
    permission_classes = (AdminWriteOnly, )
    filter_class = CategoryFilter
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
