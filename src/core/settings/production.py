"""
Django production settings for core project
"""

import os
import json
import dj_database_url
from django_sharding_library.settings_helpers import database_config, database_configs
SECRET_KEY = os.environ.get(
    "SECRET_KEY", 'iw7&5xlpe_*jk*vd=0z4hs#o=kg1g9ze7xx@528o3tq!(h!qx$')

DEFAULT_CONNECTION = dj_database_url.parse(os.environ.get("DATABASE_URL"))
DATABASES = database_configs(databases_dict={
    'unsharded_databases': [
    ],
    'sharded_databases': [
        {
            'name': 'default',
            'environment_variable': 'DATABASE_URL',
            'default_database_url':  'postgres://admin:admin@localhost:5432/contact1'
        },
        {
            'name': 'contact2',
            'environment_variable': 'HEROKU_POSTGRESQL_SILVER_URL',
            'default_database_url': 'postgres://admin:admin@localhost:5432/contact2'
        },
    ]
})
DEBUG = True if (os.environ.get("DEBUG", "true").lower() == "true") else False
ALLOWED_HOSTS = json.loads(os.environ.get("ALLOWED_HOSTS", "[\"*\"]"))

DOMAIN_NAME = os.environ.get("DOMAIN_NAME")

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
