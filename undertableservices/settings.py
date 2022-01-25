"""
Django settings for undertableservices project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3=_-1e-k1sbnndsi4je(01ever$(_b3$!-6p=i_$%+s$3-o1lb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# below I add local host to allow gitpod to work simultaneously with the deployed app
ALLOWED_HOSTS = ['undertablelabor.herokuapp.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.sites',  # call URLS when connecting via social media
    # account. good to track users activity in the website for marketing
    # statistics purposes
    'allauth',
    'allauth.account',  # login and out, user registration password resets
    'allauth.socialaccount',  # login into social media
    'home',
    'profiles',
    'contact_services',
    'checkout',

    'crispy_forms',
    'storages',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'undertableservices.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ],
        },
    },
]

#  below goes with allauth development. turn into =2 attheendof Ado project???
SITE_ID = 1

# from django-allauth website https://django-allauth.readthedocs.io/en/latest/installation.html
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

CSRF_TRUSTED_ORIGINS = ["https://8000-orange-monkey-ihvhldff.ws-us28.gitpod.io"]
# this is for cofirmation emails when a new account is created
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Code extracted from a completed project
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # this will allow email or username as username
# the following three are the basic functionality for emails when to come to creating an account
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'undertableservices.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        # below line is referring to the env variables on heroku
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
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
DATABASES = {'default': dj_database_url.parse('postgres://nwqpontrvtgjjz:e1ac892909dd789e2e21348d66ea0df5e0b938b26c17e7338b03ce31668fbc23@ec2-18-214-140-149.compute-1.amazonaws.com:5432/djn8dmvc6s4g8')}


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECRET_KEY = os.environ.get('SECRET_KEY', '')

if 'USE_AWS' in os.environ:

    # Cache control. this tells the browser to store the cache for a long time. For performance purposes
    # AWS_S3_OBJECT_PARAMETERS = {
    #     'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    #     'CacheControl': 'max-age=94608000',
    # }
    # Bucket Config.
    AWS_STORAGE_BUCKET_NAME = 'undertablelabor'
    AWS_S3_REGION_NAME = 'us-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files. this  goes with the code on custom_storage.py
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production.
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
