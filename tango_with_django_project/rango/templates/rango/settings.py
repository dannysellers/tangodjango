import os

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
# this is needed to get the absolute path, which django needs for routing

DATABASE_PATH = os.path.join(PROJECT_PATH, 'rango.db')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DATABASE_PATH,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        # 'PORT': '',                      # Set to empty string for default.
    }
}

STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
	# Strings go here like "/home/html/django_templates"
	# Use absolute paths, not relative paths
	TEMPLATE_PATH
)

STATICFILES_DIRS = (
	STATIC_PATH,
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')  # Absolute path to media dir
