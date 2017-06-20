# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 04:23
from __future__ import unicode_literals

import contact.models
import django.core.validators
from django.db import migrations, models
import django_sharding_library.fields
import django_sharding_library.id_generation_strategies


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', django_sharding_library.fields.TableShardedIDField(primary_key=True, serialize=False, source_table_name=contact.models.ShardedContactIDs, strategy=django_sharding_library.id_generation_strategies.TableStrategy(backing_model_name=contact.models.ShardedContactIDs))),
                ('user_pk', models.PositiveIntegerField()),
                ('phone', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShardedContactIDs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('stub', models.NullBooleanField(default=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]