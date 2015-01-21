import os
from configparser import RawConfigParser


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

config = RawConfigParser()
config.read(os.path.join(BASE_DIR, "lazylight", "settings.ini"))

SECRET_KEY = config.get("django", "secret_key")

# FIXME: Don't run in debug mode for production.
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    "lazylight",
    "jquery",
    "django.contrib.staticfiles",
)

MIDDLEWARE_CLASSES = ()

ROOT_URLCONF = "lazylight.urls"
WSGI_APPLICATION = "lazylight.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "HOST": config.get("database", "host"),
        "NAME": config.get("database", "name"),
        "PASSWORD": config.get("database", "password"),
        "PORT": config.get("database", "port"),
        "USER": config.get("database", "user"),
        "OPTIONS": {"autocommit": True}
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = "/static/"


BROKER_URL = config.get("celery", "broker_url")
CELERY_RESULT_BACKEND = config.get("celery", "result_backend")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_INCLUDE = ["lazylight.hardware_controller"]
