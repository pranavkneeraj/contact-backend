"""
Category Related Serializers
"""
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category.
    """
    name = serializers.SerializerMethodField('get_category_name')
    category_id = serializers.SerializerMethodField('get_custom_category_id')
    # attributes = CategoryAttributeSerializer(many=True)

    def __init__(self, *a, **k):
        if not a:
            self.fields['name'] = serializers.CharField(max_length=255)
        super().__init__(*a, **k)

    def get_category_name(self, obj):  # pylint: disable=no-self-use
        """
        Get category name.
        """
        return obj.__str__().replace('/', ' > ')

    def get_custom_category_id(self, obj):  # pylint: disable=no-self-use
        """
        Get category id.
        """
        return obj.id

    class Meta:
        model = Category
        fields = ('category_id', 'name', 'parent')
