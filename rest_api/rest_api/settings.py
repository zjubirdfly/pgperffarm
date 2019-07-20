"""
Django settings for rest_api project.

Generated by 'django-admin startproject' using Django 1.11.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# todo: add reverse, url list on the homepage
# users: everything working, just let's add a password field, change password, and revoke crud permissions to non admins
# machines: adding works, linking to username works (add email?), reports and lastest not working
# records: filters not working!!!
# branches: work, now they just need to be added
# 'detail' and 'machine-records' give 'not found' (which might be correct?)
# records-by-branch has some issue with foreign keys

import os
import datetime
import sys

from rest_api.settings_local import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n)o!k04vu3i5%1q9!b0dd3v1&)8f1-c2st)ac@%v&2do4u&9h$'

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
	'rest_framework',
	'rest_framework.authtoken',
	'corsheaders',
	'users',
	'records',
	'machines'
]


REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': (
		#'rest_framework.permissions.IsAuthenticated',
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
		'rest_framework.authentication.SessionAuthentication',
		#'rest_framework.authentication.BasicAuthentication',
	),
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 10
}


MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ORIGIN_ALLOW_ALL = True  # set to True to test the website locally while connecting remotely
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
	'http://127.0.0.1:8080',
	'http://127.0.0.1:8000',
)


ROOT_URLCONF = 'rest_api.urls'


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

WSGI_APPLICATION = 'rest_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# overridden with Postgres

# DB_ENUM --> ?

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


JWT_AUTH = {
	'JWT_ENCODE_HANDLER':
	'rest_framework_jwt.utils.jwt_encode_handler',

	'JWT_DECODE_HANDLER':
	'rest_framework_jwt.utils.jwt_decode_handler',

	'JWT_PAYLOAD_HANDLER':
	'rest_framework_jwt.utils.jwt_payload_handler',

	'JWT_PAYLOAD_GET_USER_ID_HANDLER':
	'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

	'JWT_RESPONSE_PAYLOAD_HANDLER':
	'rest_framework_jwt.utils.jwt_response_payload_handler',

	'JWT_SECRET_KEY': SECRET_KEY,
	'JWT_GET_USER_SECRET_KEY': None,
	'JWT_PUBLIC_KEY': None,
	'JWT_PRIVATE_KEY': None,
	'JWT_ALGORITHM': 'HS256',
	'JWT_VERIFY': True,
	'JWT_VERIFY_EXPIRATION': True,
	'JWT_LEEWAY': 0,
	'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
	'JWT_AUDIENCE': None,
	'JWT_ISSUER': None,

	'JWT_ALLOW_REFRESH': False,
	'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

	'JWT_AUTH_HEADER_PREFIX': 'Bearer',
	'JWT_AUTH_COOKIE': None,
}




CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT',
	'VIEW',
)


CORS_ALLOW_HEADERS = (
	'XMLHttpRequest',
	'X_FILENAME',
	'accept-encoding',
	'authorization',
	'content-type',
	'dnt',
	'origin',
	'user-agent',
	'x-csrftoken',
	'x-requested-with',
	'Pragma',
)


DB_ENUM = {
    "general_switch": {
        "on": 1,
        "off": 2
    },
    "mode": {
        "simple": 1,
        "other": 2
    },
    "machine_state": {
        "prohibited": -1,
        "pending": 0,
        "active": 1,
    },
    "status": {
        "none": -1,
        "improved": 1,
        "quo": 2,
        "regressive": 3
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
