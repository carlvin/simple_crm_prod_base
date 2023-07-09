import os
from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env(
    DEBUG=(bool, False)
)

READ_DOT_ENV_FILE = env.bool("READ_DOT_ENV_FILE",default=False)

if READ_DOT_ENV_FILE:
    environ.Env.read_env(
        BASE_DIR / "../.env"
    )

# my_variable = env('DJANGO_SETTINGS_MODULE')
# print(f"By:Carlvin:: This is the Module setting running:{ my_variable }")
# # Get the value of an environmental variable
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

# # Check if the environmental variable exists and retrieve its value
# if secret_key:
#     print(f"The SECRET_KEY is: {secret_key}")
# else:
#     print("SECRET_KEY is not set.")



ALLOWED_HOSTS = ['127.0.0.1', 'localhost',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_htmx',
    'django_htmx_refresh',

    'client_relationship_manager',
    'agents',

    'crispy_forms',
    'crispy_tailwind',
]

# This setting is used by HtmxResponseMiddleware
HTMX_APPS = [
    'crm',
    'agents',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'django_htmx_refresh.middleware.HtmxResponseMiddleware',
]

ROOT_URLCONF = 'config.urls'

# BASE_TEMPLATES_DIR = BASE_DIR / 'templates'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / '../templates',
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "../static"
]
STATIC_ROOT = "static_root"

AUTH_USER_MODEL = 'client_relationship_manager.User'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'

LOGOUT_REDIRECT = "/"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

EMAIL_HOST = "smtp.zoho.com"
EMAIL_HOST_USER = "info@carlhub.com"
EMAIL_HOST_PASSWORD = "zp!8lCkv"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "info@carlhub.com"
