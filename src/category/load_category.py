"""
Module for load category from file.
"""
import os
import json
from category.models import (Category, Attribute, CategoryAttribute)

amazon_ids = Category.objects.values_list('amazon_id', flat=True)  # pylint: disable=invalid-name


def insert_into_db(category, model, categories, parent=None):
    """
    Insert catgory into db.
    """
    try:
        category_obj = Category.objects.get(
            name=category, amazon_id=categories[category]['_id'],
            parent=parent)
    except Category.DoesNotExist:
        category_obj = model(name=category,
                             amazon_id=categories[category]['_id'],
                             parent=parent)
        category_obj.save()
    for children in categories[category].get('children', {}):
        insert_into_db(children, model, categories[category][
            'children'], category_obj)


def get_valid_type(values):
    """
    Get a valide type.
    """
    try:
        value_type = 'number' if (
            'integer' in values[0] or 'numeric value' in values[0]) else 'choice'
    except TypeError:
        value_type = 'choice'
    return value_type, (values if value_type == 'choice' else [])


def insert_attribute_into_db(attribute_obj, categories, accepted_values):
    """
    Insert attribute into database.
    """
    records = []
    for category in categories:
        try:
            categoryattribute = CategoryAttribute.objects.get(attribute_id=attribute_obj.id,  # pylint: disable=unused-variable
                                                              category_id=category.id)
        except CategoryAttribute.DoesNotExist:
            value_type, choices = get_valid_type(
                accepted_values[category.amazon_id])
            records.append(CategoryAttribute(category=category,
                                             attribute=attribute_obj,
                                             value_type=value_type,
                                             choices=choices))
    CategoryAttribute.objects.bulk_create(records)


def _load_category():
    """
    Load category.
    """
    path = os.path.dirname(os.path.abspath(__file__))

    json_file = open(os.path.join(path, "migrations/category.json"), "r")
    categories = json.loads(json_file.read())
    for category in categories:
        insert_into_db(category, Category, categories)
    json_file = open(os.path.join(path, "migrations/attributes.json"), "r")
    attributes = json.loads(json_file.read())
    for attribute in attributes:
        try:
            attribute_obj = Attribute.objects.get(name=attribute)
        except Attribute.DoesNotExist:
            attribute_obj = Attribute(name=attribute)
            attribute_obj.save()  # pylint: disable=no-member
        categories = Category.objects.filter(
            amazon_id__in=list(attributes[attribute]['categories'].keys())
        )
        insert_attribute_into_db(
            attribute_obj, categories, attributes[attribute]['categories']
        )
