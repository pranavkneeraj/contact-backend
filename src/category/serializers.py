"""
Category Related Serializers
"""
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category.
    """
    #name = serializers.SerializerMethodField('get_category_name')
    #category_id = serializers.SerializerMethodField('get_custom_category_id')
    # attributes = CategoryAttributeSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'parent')
