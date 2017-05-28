"""
Custom Pagination for app
"""
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class
    """
    page_size = 10
    page_size_query_param = 'page-size'
    max_page_size = 100
