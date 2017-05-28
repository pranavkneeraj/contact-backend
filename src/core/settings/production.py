"""
Django production settings for core project
"""

import os
import json
import dj_database_url

SECRET_KEY = os.environ.get(
    "SECRET_KEY", 'iw7&5xlpe_*jk*vd=0z4hs#o=kg1g9ze7xx@528o3tq!(h!qx$')

DEFAULT_CONNECTION = dj_database_url.parse(os.environ.get("DATABASE_URL"))
DATABASES = {"default": DEFAULT_CONNECTION}
DEBUG = True if (os.environ.get("DEBUG", "true").lower() == "true") else False
ALLOWED_HOSTS = json.loads(os.environ.get("ALLOWED_HOSTS", "[\"*\"]"))

DOMAIN_NAME = os.environ.get("DOMAIN_NAME")

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
