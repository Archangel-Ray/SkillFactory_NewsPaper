"""
Django settings for Publications project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yuc9^%o9kwtvz!#yfij9s#8a)o5@l(9+7$nevoq61uj)tpv5*!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',

    'ckeditor',

    "board",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # добавление учётной записи в базу:
    "allauth.account.middleware.AccountMiddleware",
]

SITE_ID = 1  # номер сайта (если их будет несколько)

ROOT_URLCONF = "Publications.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "Publications.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
# STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = '/accounts/login/'  # ссылка на форму аутентификации
LOGIN_REDIRECT_URL = '/'  # ссылка после аутентификации

AUTHENTICATION_BACKENDS = [
    # Вход в систему по имени пользователя в администраторе Django, независимо от `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # специальные методы аутентификации `allauth`, такие, как вход по электронной почте.
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True  # почта обязательна
ACCOUNT_UNIQUE_EMAIL = True  # поле почты уникально
ACCOUNT_USERNAME_REQUIRED = False  # выключает обязательное заполнение имени
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # метод аутентификации через поле почты
ACCOUNT_EMAIL_VERIFICATION = 'none'  # проверка почты (не знаю как подключить)

# настройка отправки писем по эл.почте
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = open(
    "G:/Python_projects/all_secret_codes_are_here/Yandex email/login.txt"
).read()
EMAIL_HOST_PASSWORD = open(
    "G:/Python_projects/all_secret_codes_are_here/Yandex email/password.txt"
).read()
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = open(
    "G:/Python_projects/all_secret_codes_are_here/Yandex email/email.txt"
).read()
SERVER_EMAIL = DEFAULT_FROM_EMAIL  # адрес сервера
ADMINS = (("admin", DEFAULT_FROM_EMAIL),)  # список админов
