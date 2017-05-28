"""
Django local settings template for core project
"""

DEBUG = True

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db-name>',
        'USER': '',
        'PASSWORD': '',
    }
}

MWS = {
    'ACCESS_KEY': '',
    'SECRET_KEY': ''
}

ALLOWED_HOSTS = [""]
DOMAIN_NAME = ""
FRONTEND_DOMAIN_NAME = ""
KEY = "Boom Boom"
EMAIL_HOST_USER = ''
# Must generate specific password for your app in [gmail settings][1]
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

AWS_STORAGE_BUCKET_NAME = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
