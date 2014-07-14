from utils import LOCAL

SITE_ID = 1
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = True
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'wowadb',
#         'USER': 'wowa_u',
#         'PASSWORD': 'wowa_u',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': LOCAL('db.sqlite'),
    }
}

MORE_INSTALLED_APPS = (
    'debug_toolbar',
)

#settings this for debug tools
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')
