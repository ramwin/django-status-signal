"""
Django settings for test_example_project project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z!zmo9_fh%cxld(5cts-!a@7l@_$!xg(@hq#-wz$ol0pmxg4hj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_example_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'test_example_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
      'verbose': {
          'format': ('[%(levelname)5s] %(asctime)s %(filename)s '
                     '%(funcName)s (line: %(lineno)d)'
                     '    %(message)s'),
      },
      'simple': {
          'format': '[%(levelname)s] %(message)s ',
      },
  },
  'handlers': {
      'error_file': {
          'level': "ERROR",
          'class': 'logging.FileHandler',
          'filename': 'log/error.log',
          'formatter': 'verbose',
      },
      'warning_file': {
          'level': "WARNING",
          'class': 'logging.handlers.RotatingFileHandler',
          'filename': 'log/warning.log',
          'maxBytes': 1024 * 1024 * 10,
          'backupCount': 20,
          'formatter': 'verbose',
      },
      'info_file': {
          'level': "INFO",
          'class': 'logging.handlers.RotatingFileHandler',
          'maxBytes': 1024 * 1024 * 10,
          'backupCount': 20,
          'filename': 'log/info.log',
          'formatter': 'verbose',
      },
      'debug_file': {
          'level': "DEBUG",
          'class': 'logging.handlers.RotatingFileHandler',
          'maxBytes': 1024 * 1024 * 10,
          'backupCount': 20,
          'filename': 'log/debug.log',
          'formatter': 'verbose',
      },
      'console': {
          'class': 'logging.StreamHandler',
          'formatter': 'verbose',
      },
  },
  'loggers': {
      'default': {
          'handlers': ['debug_file', 'info_file',
                       'warning_file', 'error_file', 'console'],
          'level': "INFO",
      },
      'django': {
          'handlers': ['debug_file', 'info_file',
                       'warning_file', 'error_file', 'console'],
          'level': "INFO",
      },
      'test_app': {
          'handlers': ['debug_file', 'info_file',
                       'warning_file', 'error_file', 'console'],
          'level': "INFO",
      },
  },
}
