from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db import models
from django_sharding_library.decorators import shard_storage_config
from django_sharding_library.models import ShardedByMixin
from django_sharding_library.signals import save_shard_handler


@shard_storage_config()
class User(AbstractUser, ShardedByMixin):
    pass


@receiver(models.signals.pre_save, sender=User)
def shard_handler(sender, instance, **kwargs):
    print(kwargs)
    save_shard_handler(sender, instance, **kwargs)
