# -*- coding: utf-8 -*-
"""
    Settings
    ~~~~~~~~~~~~~~

    A divided settings module.

    :copyright: (c) 2014 by arruda.
"""

import sys
import os


MAIN_APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_ROOT = os.path.dirname(MAIN_APP_ROOT)
SITE_ROOT = os.path.dirname(DJANGO_ROOT)
sys.path.append(DJANGO_ROOT)


SECRET_KEY = 'o2ysng32bvj1^=bpyx80*^8vfywhsts4pdehi5j@v)$fd9f-p+'

from config import *
from installed_apps import *
from logging import *

ENV_SETTINGS = os.environ.get('ENV_SETTINGS', 'local')

NO_DEPRECATION_WARNINGS = False

if ENV_SETTINGS == 'local':
    NO_DEPRECATION_WARNINGS = True
    from env_local import *
elif ENV_SETTINGS == 'docker':
    from env_docker import *
elif ENV_SETTINGS == 'heroku':
    from env_heroku import *


INSTALLED_APPS += MORE_INSTALLED_APPS

if NO_DEPRECATION_WARNINGS:
    import warnings
    warnings.simplefilter('ignore', DeprecationWarning)
