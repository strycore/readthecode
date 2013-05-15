# -*- coding: utf-8 -*-
from os.path import join, dirname, abspath

PROJECT_ROOT = dirname(dirname(abspath(__file__)))
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Mathieu Comandon', 'strider@strycore.com'),
)
MANAGERS = ADMINS
SITE_ID = 1
ROOT_URLCONF = 'readthecode.urls'
WSGI_APPLICATION = 'readthecode.wsgi.application'
SECRET_KEY = 'm35=*=ala2_gd)z_g&9bf8s405k^vv5@xz-o8vx5i&ssv$0=%q'
ALLOWED_HOSTS = (
    'readthecode.strycore.com',
    'readthecode.org',
    'www.readthecode.org'
)

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}

# Apps
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'compressor',
    'south',
    'django_celery',

    'main',
)

# Nosetests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Localization
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static / Media files
MEDIA_ROOT = join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    join(PROJECT_ROOT, 'components'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Templates
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    join(PROJECT_ROOT, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
)

# Middleware
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# Authentication / Registration (may need Django-Registration)
ACCOUNT_ACTIVATION_DAYS = 3
LOGIN_REDIRECT_URL = "/"

# Email
DEFAULT_FROM_EMAIL = "admin@readthecode.org"
EMAIL_SUBJECT_PREFIX = "readthecode"

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'include_html': True,
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'syslog'],
            'level': 'ERROR',
        },
        'main': {
            'handlers': ['mail_admins', 'syslog'],
            'level': 'ERROR',
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
