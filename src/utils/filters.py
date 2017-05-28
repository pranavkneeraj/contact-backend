"""
shared filter for Model filtering
"""
import django_filters
from django.db.models import Q
from django.contrib.postgres.forms import SimpleArrayField


class SimpleProductArrayFilter(django_filters.Filter):
    """
    Simple array field for product model.
    """
    field_class = SimpleArrayField

    def filter(self, qs, value):  # pylint: disable=method-hidden
        if len(value) == 1:
            args = (Q(sku_number__icontains=value[0]) | Q(
                name__icontains=value[0]))
            return qs.filter(args)
        elif len(value) > 0:
            return qs.filter(**{'%s__in' % self.name: value})
        return qs
