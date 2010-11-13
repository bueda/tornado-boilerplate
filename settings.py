import os
import logging, logging.handlers

import environment

import comrade.log.settings
from comrade.core.settings import *

ROOT = os.path.dirname(os.path.abspath(__file__))

MEDIA_ROOT = path(ROOT, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin'

# Version Information

import subprocess
GIT_COMMIT = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
    stdout=subprocess.PIPE).communicate()[0].strip()
del subprocess

# Database

DATABASES = {}

if DEPLOYMENT == DeploymentType.PRODUCTION:
    DATABASES['default'] = {
        'NAME': 'boilerplate',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'your-database.com',
        'PORT': '',
        'USER': 'boilerplate',
        'PASSWORD': 'your-password'
    }
elif DEPLOYMENT == DeploymentType.DEV:
    DATABASES['default'] = {
        'NAME': 'boilerplate_dev',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'your-database.com',
        'PORT': '',
        'USER': 'boilerplate',
        'PASSWORD': 'your-password'
    }
elif DEPLOYMENT == DeploymentType.STAGING:
    DATABASES['default'] = {
        'NAME': 'boilerplate_staging',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'your-database.com',
        'PORT': '',
        'USER': 'boilerplate',
        'PASSWORD': 'your-password'
    }
else:
    DATABASES['default'] = {
        'NAME': 'db',
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': ''
    }

# Message Broker (for Celery)

CELERY_ALWAYS_EAGER = DEPLOYMENT == DeploymentType.SOLO
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "boilerplate"
BROKER_PASSWORD = "boilerplate"
BROKER_VHOST = "boilerplate"
CELERY_RESULT_BACKEND = "amqp"

# South

SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

# Logging

SYSLOG_FACILITY = logging.handlers.SysLogHandler.LOG_LOCAL0
SYSLOG_TAG = "boilerplate"

# See PEP 391 and log_settings.py for formatting help.  Each section of LOGGING
# will get merged into the corresponding section of log_settings.py.
# Handlers and log levels are set up automatically based on LOG_LEVEL and DEBUG
# unless you set them here.  Messages will not propagate through a logger
# unless propagate: True is set.
LOGGERS = {
    'loggers': {
        'boilerplate': {},
    },
}

comrade.log.settings.initialize_logging(SYSLOG_TAG, SYSLOG_FACILITY, LOGGERS,
        LOG_LEVEL, USE_SYSLOG)

# Cache Backend

CACHE_TIMEOUT = 3600

# Debug Toolbar

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

# Application Settings

SECRET_KEY = 'TODO-generate-a-new-secret-key'

middleware_list = [
    'commonware.log.ThreadRequestMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'comrade.core.middleware.HttpMethodsMiddleware',
]

if DEPLOYMENT != DeploymentType.SOLO:
    middleware_list += [
        'django.middleware.transaction.TransactionMiddleware',
        'commonware.middleware.SetRemoteAddrFromForwardedFor',
    ]
else:
    middleware_list += [
        'comrade.core.middleware.ArgumentLogMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

MIDDLEWARE_CLASSES = tuple(middleware_list)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',

    'comrade.core.context_processors.default',
    'django.core.context_processors.media',
)

TEMPLATE_DIRS = (
    path(ROOT, 'templates')
)

apps_list = [
        'django.contrib.auth',
        'django.contrib.admin',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.markup',
        'django.contrib.messages',

        'TODO',
        'your',
        'apps',
        'here',
]

if DEPLOYMENT == DeploymentType.SOLO:
    apps_list += [
        'django_extensions',
        'debug_toolbar',
        'django_nose',
    ]

INSTALLED_APPS = tuple(apps_list)

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
