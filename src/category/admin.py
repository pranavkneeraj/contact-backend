"""
Category admin
"""
from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin
    """
    pass

admin.site.register(Category, CategoryAdmin)
