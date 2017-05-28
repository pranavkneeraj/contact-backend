"""
Category related Models
"""
from django.db import models


class Category(models.Model):

    """
    Product Category Model
    """
    name = models.CharField(
        max_length=255, db_index=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True)

    def __str__(self):
        return '%s/%s' % (self.parent, self.name) if self.parent else self.name

    class Meta:
        unique_together = ('name', 'parent')
