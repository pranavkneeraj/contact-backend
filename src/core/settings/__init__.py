"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django_sharding_library.sharding_functions import ModBucketingStrategy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


try:
    from .local import *  # pylint:disable=C0413,wildcard-import
except ImportError:
    from .production import *  # pylint:disable=wildcard-import


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'corsheaders',
    'rest_framework',
    'knox',
    'utils',
    'django_sharding',
    'authentication',
    'contact',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '..', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.APPLICATION'


# Custom AUthentication

AUTHENTICATION_BACKENDS = ('authentication.auth_backend.CustomAuthBackend', )
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'authentication.User'
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
APPEND_SLASH = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'knox.auth.TokenAuthentication'
    ),
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'rest_framework.filters.DjangoFilterBackend',
    # )
}


# REST FRAMEWORK KONX Settings
REST_KNOX = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64,
    'TOKEN_TTL': datetime.timedelta(hours=12),
    'USER_SERIALIZER': 'knox.serializers.UserSerializer',
}
DATABASE_ROUTERS = ['django_sharding_library.router.ShardedRouter']

#DATABASE_ROUTERS = ['core.routers.CoreRouter', ]

BLOCKSIZE = 16

# CORS Settings

CORS_ORIGIN_ALLOW_ALL = True

CORS_REPLACE_HTTPS_REFERER = True

CORS_ALLOW_METHODS = (
    'POST',
    'PUT',
    'PATCH',
    'OPTIONS'
)

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)

# Email Setting

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static'),
    os.path.join(BASE_DIR, '..', 'static/ui/node_modules'),

)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')


ANGULAR_URL = '/ng/'

ANGULAR_ROOT = os.path.join(BASE_DIR, '..', 'static/ui')

#API_URL =   "https://product-services.herokuapp.com/"
API_URL = "/"

# DJANGO_SHARDING_SETTINGS = {"default": {
#     "BUCKETING_STRATEGY": ModBucketingStrategy('default', DATABASES)}}
