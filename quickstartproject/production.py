from .settings import *
import os
from pathlib import Path

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = ['*']

# WhiteNoise configuration
MIDDLEWARE = [                                                                   
    'django.middleware.security.SecurityMiddleware',
# Add whitenoise middleware after the security middleware                             
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',                      
    'django.middleware.common.CommonMiddleware',                                 
    'django.middleware.csrf.CsrfViewMiddleware',                                 
    'django.contrib.auth.middleware.AuthenticationMiddleware',                   
    'django.contrib.messages.middleware.MessageMiddleware',                      
    'django.middleware.clickjacking.XFrameOptionsMiddleware',                    
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = r'/static/'


MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_URL = r'/media/'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '275595339bde640fe4a5fa39ac67bfadd8f251eff03b3521f1265edffbb305c6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    'https://petmedvida.azurewebsites.net',
    'http://127.0.0.1:8000/',
    # add any other trusted origins as needed
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registro_de_animais',
    'rolepermissions',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    
]

ROOT_URLCONF = 'quickstartproject.urls'

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

WSGI_APPLICATION = 'quickstartproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'PI_S2G7',
        'PASSWORD': '72N96a&x',
        'HOST': 'petmedvida.postgres.database.azure.com',
        'PORT': '',
        'OPTIONS': {
            'sslmode': 'require',
        }
    },
    'dev': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
# STATIC_URL = r'/static/'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = r'/static/'


MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_URL = r'/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROLEPERMISSIONS_MODULE = 'registro_de_animais.roles'

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

AZURE_ACCOUNT_NAME = 'petmedvidastorage'
AZURE_ACCOUNT_KEY = 'hektiopqIovp1q4sz8wfPHX3TghKOv5sYiKeIRNOwVBm6LYGAMIH9tGCd761wyroDf9S6BT8x9/1+ASt2YdS5g=='
AZURE_CONTAINER = 'fotosdepets'
