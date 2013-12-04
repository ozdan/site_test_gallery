# Django settings for site_test_gallery project.
import os
from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.core.urlresolvers import reverse

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'site_test_gallery',
        'USER': 'site_test_gallery',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

ALLOWED_HOSTS = []
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
VIRTUAL_ENV = os.environ['VIRTUAL_ENV']
MEDIA_ROOT = os.path.join(VIRTUAL_ENV, 'www', 'media')
STATIC_ROOT = os.path.join(VIRTUAL_ENV, 'www', 'static')

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'uo-aw$s9d&&j^_9293z&p+8k7_^&f5jt3gwe1s%c21u_b_y+h$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'site_test_gallery.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'site_test_gallery.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'test_gallery',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'django_extensions',
    'sorl.thumbnail',
)

LOGIN_REDIRECT_URL = reverse('MyGalleryList')
