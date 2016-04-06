# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from huey import RedisHuey

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#r65fsg)wsk&cs8m^i)@##7-wg=#z=*b_)a82#5z#4%&!j_9=6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'flat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'rest_framework',
    'channels',
    'huey.contrib.djhuey',
)

INSTALLED_APPS += (
    'oliver_screen',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'oliversite.urls'
WSGI_APPLICATION = 'oliversite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Oslo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Last.FM
LASTFM_DEFAULT_USERNAME = 'kakdns'
# Get these from http://www.last.fm/api/account
LASTFM_API_KEY = ''
LASTFM_API_SECRET = ''

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
        "ROUTING": "oliversite.routing.channel_routing",
    },
}
OLIVER_WS_GROUP = 'screens'
OLIVER_LASTFM_POLL_INTERVAL = 10  # seconds

# HUEY = {
#     'name': 'oliverscreen',
#     'connection': {'host': 'localhost', 'port': 6379},
#     'consumer': {'workers': 1, 'worker_type': 'process'},
# }

HUEY = RedisHuey('oliverscreen', result_store=True)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
    }
}

# Local settings
try:
    from .local_settings import *
except ImportError:
    pass
