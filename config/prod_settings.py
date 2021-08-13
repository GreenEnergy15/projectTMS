import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o6aa&&*+v)udu7ohlh)yi$0&@^e%_t16hqcvxqo5yonnvr%n9&u'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST' : 'localhost',
        'PORT': '5422',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
