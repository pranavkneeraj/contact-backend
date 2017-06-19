# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django_sharding_library.fields
import django_sharding_library.id_generation_strategies


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20170617_0559'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShardedContactEmailIDs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('stub', models.NullBooleanField(default=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShardedContactPhoneIDs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('stub', models.NullBooleanField(default=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='contactemail',
            name='id',
            field=django_sharding_library.fields.TableShardedIDField(primary_key=True, serialize=False, source_table_name='contact.ShardedContactEmailIDs', strategy=django_sharding_library.id_generation_strategies.TableStrategy(backing_model_name='contact.ShardedContactEmailIDs')),
        ),
        migrations.AlterField(
            model_name='contactphone',
            name='id',
            field=django_sharding_library.fields.TableShardedIDField(primary_key=True, serialize=False, source_table_name='contact.ShardedContactPhoneIDs', strategy=django_sharding_library.id_generation_strategies.TableStrategy(backing_model_name='contact.ShardedContactPhoneIDs')),
        ),
    ]
