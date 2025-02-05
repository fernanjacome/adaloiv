"""
Django settings for adaloivback project.

Generated by 'django-admin startproject' using Django 5.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path


from datetime import timedelta
from corsheaders.defaults import default_headers

# Configuración de JWT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",  # Permite el acceso sin necesidad de autenticación
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=15
    ),  # Tiempo de expiración del access token
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=1
    ),  # Tiempo de expiración del refresh token
    "ROTATE_REFRESH_TOKENS": True,  # Si se quiere rotar el refresh token
    "BLACKLIST_AFTER_ROTATION": True,  # Si se quiere hacer blacklist de los refresh tokens
}
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-1n$7!nm0kk_8yp2=!irt!f#%#8kz2xc5a&nytplrx8m55oq%*j"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api",
    "corsheaders",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

# Permitir los orígenes de tu frontend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend de React en desarrollo
    "http://localhost:3001",  # Frontend de React en desarrollo
]

# Permitir las cabeceras necesarias
CORS_ALLOW_HEADERS = list(default_headers) + [
    "Authorization",  # Permitir la cabecera Authorization para JWT
    "Content-Type",  # Asegúrate de permitir Content-Type si se usan solicitudes JSON
    "Accept",  # Asegura que la cabecera Accept esté permitida
]

ROOT_URLCONF = "adaloivback.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "adaloivback.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "mssql",
#         "NAME": "ADALOIV2",
#         "USER": "extreme",
#         "PASSWORD": "alexsoft",
#         "HOST": "PC-FJACOME",
#         "PORT": "",
#         "OPTIONS": {
#             "driver": "ODBC Driver 17 for SQL Server",
#         },
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'ADALOIV2',
        'USER': '',  # Deja esto vacío para la autenticación de Windows
        'PASSWORD': '',  # Deja esto vacío para la autenticación de Windows
        'HOST': 'JAZAT\\FJACOME',
        'PORT': '',  # Por defecto es 1433, puedes dejarlo vacío si usas el puerto por defecto
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'Trusted_Connection=yes;',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
