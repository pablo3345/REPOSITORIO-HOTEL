"""
Django settings for ProyectoWeb_hotel project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.contrib.messages import constants as mensaje_de_error



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@z7_d**)$q+apty(csu=)^q(k2l*x)g-)=xt^g0*78r(65k2x+'

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
    'proyectoWebApp',
    'habitacion',
    'contrato',
    'crispy_forms',
    "crispy_bootstrap5", #para el formulario crispy de bootstra5
    'panel_de_admin',
   
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

ROOT_URLCONF = 'ProyectoWeb_hotel.urls'

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

WSGI_APPLICATION = 'ProyectoWeb_hotel.wsgi.application'
#contraseña de postgres 10 (12345211)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hotel_admin',
        'USER': 'hotel1',
        'PASSWORD': 'hotelhotel1',
        'HOST': '127.0.0.1',
        'PORT': '3306',


    }

}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-eu'
#TIME_ZONE = 'UTC'
TIME_ZONE='America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

#USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/' # esto seria la url publica para que django encuentre las imagenes
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # aca le decimos donde debe ir a buscar django los archivos media

CRISPY_TEMPLATE_PACK= 'bootstrap5' # es para decirle que cargue este paquete crispy en boostrap5


MESSAGE_TAGS = { # TAGS viene de etiqueta "debug" nombro la etiqueta, abajo escribi todas las etiquetas x si mas adelante las voy a usar

mensaje_de_error.DEBUG: 'alert-dark',
mensaje_de_error.INFO: 'alert-info',
mensaje_de_error.SUCCESS: 'alert-success',
mensaje_de_error.WARNING: 'alert-warning',
mensaje_de_error.ERROR:'alert-danger',


}