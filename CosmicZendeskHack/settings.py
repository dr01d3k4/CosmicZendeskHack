"""
Django settings for CosmicZendeskHack project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os;
BASE_DIR = os.path.dirname(os.path.dirname(__file__));
SETTINGS_DIR = os.path.dirname(__file__);
PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir));



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "87o=yu=dz5l_2c_b6tm8tr(e(_xxp0pio(io*qo5u%pp5fv9y_";



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True;




TEMPLATE_DEBUG = True;

ALLOWED_HOSTS = [".dylanmaryk.com", "dr01d3k4.pythonanywhere.com"];


# Application definition

INSTALLED_APPS = (
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"cosmic_hack"
);



MIDDLEWARE_CLASSES = (
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
);



ROOT_URLCONF = "CosmicZendeskHack.urls";

WSGI_APPLICATION = "CosmicZendeskHack.wsgi.application";


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": os.path.join(BASE_DIR, "db.sqlite3"),
	}
};

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = "en-us";

TIME_ZONE = "UTC";

USE_I18N = True;

USE_L10N = True;

USE_TZ = True;


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_PATH = os.path.join(PROJECT_PATH, "app/www/");
JS_PATH = os.path.join(STATIC_PATH, "js");
STATIC_URL = "/static/";
STATICFILES_DIRS = (
	STATIC_PATH,
);


TEMPLATE_PATH = os.path.join(PROJECT_PATH, "app");
TEMPLATE_DIRS = (
	TEMPLATE_PATH,
);


MEDIA_URL = "/media/";
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media");