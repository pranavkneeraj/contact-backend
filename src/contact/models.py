from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from .validators import user_foreign_key_valiator
from django_sharding_library.decorators import model_config
from django_sharding_library.fields import TableShardedIDField
from django_sharding_library.models import TableStrategyModel


class ShardedContactIDs(TableStrategyModel):
    pass


class ShardedContactPhoneIDs(TableStrategyModel):
    pass


class ShardedContactEmailIDs(TableStrategyModel):
    pass


@model_config(shard_group='default', sharded_by_field='user')
class Contact(models.Model):
    """
    Contact list of users
    """
    id = TableShardedIDField(
        primary_key=True, source_table_name='contact.ShardedContactIDs')
    user = models.PositiveIntegerField()
    name = models.CharField(max_length=100)

    def get_shard(self):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=self.user).shard

    @staticmethod
    def get_shard_from_id(user_pk):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=user_pk).shard

    def save(self, *args, **kwargs):
        shard = self.get_shard()
        kwargs['using'] = shard
        super(Contact, self).save(*args, **kwargs)


class ContactPhone(models.Model):
    CONTACT_TYPE_PERSONAL = 'personal'
    CONTACT_TYPE_WORK = 'work'
    CONTACT_TYPE_HOME = 'home'
    CONTACT_TYPE_CUSTOM = 'custom'

    CONTACT_TYPE_CHOICES = (
        (CONTACT_TYPE_PERSONAL, 'Personal'), (CONTACT_TYPE_WORK, 'Work'), (CONTACT_TYPE_HOME, 'Home'), (CONTACT_TYPE_CUSTOM, 'Custom'))
    id = TableShardedIDField(
        primary_key=True, source_table_name='contact.ShardedContactPhoneIDs')
    contact = models.ForeignKey(Contact)
    contact_type = models.CharField(
        choices=CONTACT_TYPE_CHOICES, default=CONTACT_TYPE_PERSONAL, max_length=100)
    custom_type = models.CharField(max_length=100, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # validators should be a list
    phone = models.CharField(max_length=20, validators=[phone_regex])

    def save(self, *args, **kwargs):
        if kwargs.get('using'):
            shard = kwargs.get('using')
        else:
            shard = self.contact.get_shard()
        kwargs['using'] = shard
        super(ContactPhone, self).save(*args, **kwargs)


class ContactEmail(models.Model):
    CONTACT_TYPE_PERSONAL = 'personal'
    CONTACT_TYPE_WORK = 'work'
    CONTACT_TYPE_HOME = 'home'
    CONTACT_TYPE_CUSTOM = 'custom'

    CONTACT_TYPE_CHOICES = (
        (CONTACT_TYPE_PERSONAL, 'Personal'), (CONTACT_TYPE_WORK, 'Work'), (CONTACT_TYPE_HOME, 'Home'), (CONTACT_TYPE_CUSTOM, 'Custom'))
    id = TableShardedIDField(
        primary_key=True, source_table_name='contact.ShardedContactEmailIDs')
    contact_type = models.CharField(
        choices=CONTACT_TYPE_CHOICES, default=CONTACT_TYPE_PERSONAL, max_length=100)
    custom_type = models.CharField(max_length=100, null=True)
    contact = models.ForeignKey(Contact)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        if kwargs.get('using'):
            shard = kwargs.get('using')
        else:
            shard = self.contact.get_shard()
        kwargs['using'] = shard
        super(ContactEmail, self).save(*args, **kwargs)
