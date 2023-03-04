"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


from pathlib import Path
from dotenv import load_dotenv
import os


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w5)7)h0^&yd%-2id$3fj7ym2qk2gxvesm4v4i%qy#1h@(q+ij@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'django_filters',
    'fpages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
    'django_celery_beat',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'basic.middlewares.TimezoneMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

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
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization 'ru-ru' 'en-us' 'es-ar'
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGES = [
    ('en-us', 'English'),
    ('es-ar', 'Spanish'),
    ('ru-ru', 'Russian'),
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/news"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = 60
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_EMAIL_HOST')

SITE_URL = 'http://127.0.0.1:8000'


APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'

APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT': 60,
    }
}

ADMINS = [('Oleg', 'rex696@yandex.ru')]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
            'django': {
                'handlers': [
                    'my_console',
                    'my_general',
                    'my_console_warning',
                    'my_console_error_critical'
                ],
                'level': 'DEBUG',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['my_mail_admins', 'my_errors'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.server': {
                'handlers': ['my_mail_admins', 'my_errors'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.template': {
                'handlers': ['my_errors'],
                'level': 'ERROR',
            },
            'django.security': {
                'handlers': ['my_security'],
                'level': 'INFO',
            },
            'django.db.backends': {
                'handlers': ['my_errors'],
                'level': 'ERROR',
            },
        },
    'handlers': {
            'my_console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'first',
                'filters': ['require_debug_true'],
            },
            'my_console_warning': {
                'level': 'WARNING',
                'class': 'logging.StreamHandler',
                'formatter': 'second',
                'filters': ['require_debug_true'],
            },
            'my_console_error_critical': {
                'level': 'ERROR',
                'class': 'logging.StreamHandler',
                'formatter': 'third',
                'filters': ['require_debug_true'],
            },
            'my_general': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': 'temp/general.log',
                'formatter': 'first',
                'filters': ['require_debug_false'],
            },
            'my_security': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': 'temp/security.log',
                'formatter': 'fourth',
            },
            'my_mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'include_html': True,
                'formatter': 'second',
                'filters': ['require_debug_false'],
            },
            'my_errors': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': 'temp/errors.log',
                'formatter': 'third',
            },
        },
    'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },
    'formatters': {
        'first': {
            'format': '{asctime} {levelname} {message}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
        'second': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
        'third': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
        'fourth': {
            'format': '{asctime} {levelname} {module} {message}',
            'timetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
    },
}
