import os
from utils import LOCAL

SITE_ID = 1
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = True

DB_HOST = os.environ.get("DB_PORT_5432_TCP_ADDR")
DB_PORT = os.environ.get("DB_PORT_5432_TCP_PORT")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wowa_db',
        'USER': 'wowa_u',
        'PASSWORD': 'wowa_u',
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': LOCAL('db.sqlite'),
#     }
# }

MORE_INSTALLED_APPS = (
    'debug_toolbar',
)

#settings this for debug tools
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
