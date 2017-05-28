"""
Common Viewsets
"""
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .pagination import StandardResultsSetPagination


class PaginatedViewSetMixin(NestedViewSetMixin, viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Viewset for Paginated Values
    """
    pagination_class = StandardResultsSetPagination
