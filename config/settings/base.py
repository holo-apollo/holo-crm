"""
Django settings for holoapollo project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import json
import os

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

import dj_database_url
import dotenv

dotenv.load()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = dotenv.get('SECRET_KEY', default='1e5_tvt+a34)w0u7w)jyma@#it+*s4#xy55x-&f0(2r3w3(h+-')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PRODUCTION = True if dotenv.get('PRODUCTION') else False

ADMINS = [
    ('Holo', 'ira@holo-apollo.art'),
]
MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'modeltranslation',  # must be put before admin for integration
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.forms',

    # third-party
    'corsheaders',
    'django_filters',
    'djmoney',
    'raven.contrib.django.raven_compat',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'storages',
    'django_s3_collectstatic',

    # local
    'apps.common',
    'apps.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'config.context_processors.settings_vars',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = [
    'apps.users.login_backend.HoloModelBackend',
]
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')
LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('uk', _('Ukrainian')),
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
MODELTRANSLATION_DEBUG = DEBUG
MODELTRANSLATION_FALLBACK_LANGUAGES = [lang[0] for lang in LANGUAGES]

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

API_URL = dotenv.get('API_URL', default='http://localhost:8000')
UI_URL = dotenv.get('UI_URL', default='http://localhost:3000')
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# AWS
AWS_STORAGE_BUCKET_NAME = dotenv.get('AWS_STORAGE_BUCKET_NAME', default='holo-apollo-assets-eu')
AWS_S3_REGION_NAME = dotenv.get('AWS_S3_REGION_NAME', default='eu-west-1')
AWS_ACCESS_KEY_ID = dotenv.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = dotenv.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = dotenv.get('AWS_S3_CUSTOM_DOMAIN',
                                  default='s3-eu-west-1.amazonaws.com/holo-apollo-assets-eu')
AWS_PRELOAD_METADATA = True
MEDIAFILES_LOCATION = 'media-local'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

if dotenv.get('USE_AWS_STATIC'):
    STATICFILES_STORAGE = 'config.storages.StaticStorage'

STATICFILES_LOCATION = 'static-local'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s\t%(levelname)s\t%(name)s, line %(lineno)s\t'
                      '%(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django-debug.log'),
            'formatter': 'simple',
        },
    },
    'loggers': {
        'celery': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },
        '': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },
    },
}


# Celery
REDIS_URL = dotenv.get('REDIS_URL', default='redis://localhost:6379')
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']


# Emails
MAILTRAP_API_TOKEN = dotenv.get('MAILTRAP_API_TOKEN')
MAILGUN_SMTP_SERVER = dotenv.get('MAILGUN_SMTP_SERVER')
if MAILGUN_SMTP_SERVER:
    EMAIL_HOST = MAILGUN_SMTP_SERVER
    EMAIL_PORT = dotenv.get('MAILGUN_SMTP_PORT', 587)
    EMAIL_HOST_USER = dotenv.get('MAILGUN_SMTP_LOGIN', '')
    EMAIL_HOST_PASSWORD = dotenv.get('MAILGUN_SMTP_PASSWORD', '')
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
elif MAILTRAP_API_TOKEN:
    from urllib.request import urlopen, Request

    request = Request(f"https://mailtrap.io/api/v1/inboxes.json?api_token={MAILTRAP_API_TOKEN}")
    response_body = urlopen(request).read()
    credentials = json.loads(response_body)[0]

    EMAIL_HOST = credentials['domain']
    EMAIL_HOST_USER = credentials['username']
    EMAIL_HOST_PASSWORD = credentials['password']
    EMAIL_PORT = credentials['smtp_ports'][0]
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = dotenv.get('DEFAULT_FROM_EMAIL', default='info@holo-apollo.art')
SERVER_EMAIL = 'robot@holo-apollo.art'
EMAIL_SUBJECT_PREFIX = '[Holo Notification] '


# Raven
RAVEN_CONFIG = {
    'dsn': dotenv.get('SENTRY_DSN'),
}


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'apps.common.api.permissions.IsAdminOrReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'apps.common.api.pagination.PaginationWithCountHeader',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
}


REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'users.api.v1.serializers.CustomPasswordResetSerializer',
}

CURRENCIES = ('UAH',)

CORS_ORIGIN_REGEX_WHITELIST = [
    r'^(http://)?(localhost|127\.0\.0\.1)(:\d+)?$',
]

ENABLE_DDT = DEBUG and dotenv.get('ENABLE_DDT')

if ENABLE_DDT:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

    INTERNAL_IPS = type(str('c'), (), {'__contains__': lambda *a: True})()

    def show_toolbar(request):
        return True

    SHOW_TOOLBAR_CALLBACK = show_toolbar
    SHOW_COLLAPSED = True

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
