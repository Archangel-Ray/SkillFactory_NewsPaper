"""
Django settings for news_paper project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import logging
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-rm+8**+0nf&szdzmeu&if^3^60r68p*@=iu4=(11!n=#j*c*(@"

logger = logging.getLogger("Новостной портал")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["example.com", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # что бы различать сайты
    "django.contrib.sites",
    "django_filters",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # планировщик
    "django_apscheduler",
    # подключение провайдеров
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.yandex",
    "newapp",
]

SITE_ID = 1  # номер сайта для django.contrib.sites

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # учётная запись от allauth
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "news_paper.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "news_paper.wsgi.application"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, "cache_files"),
        "TIMEOUT": 60,
    }
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "/accounts/login/"  # ссылка на страницу аутентификации
LOGIN_REDIRECT_URL = "/"  # ссылка перенаправления после аутентификации

AUTHENTICATION_BACKENDS = [
    # вход в систему по имени пользователя независимо от `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # специальные методы аутентификации `allauth`,
    # такие, как вход по электронной почте.
    "allauth.account.auth_backends.AuthenticationBackend",
]
"""
Authentication backends — это компоненты, которые определяют, каким образом 
происходит проверка учётных данных пользователя.

В Django можно использовать несколько бэкендов аутентификации одновременно. 
Если стандартные методы аутентификации не удовлетворяют требования разработчика, 
можно написать собственный бэкенд. Для этого нужно создать класс, который 
наследует от django.contrib.auth.backends.BaseBackend и реализует методы 
authenticate (для проверки учётных данных) и get_user (для получения объекта 
пользователя).
"""
# переключение на аутентификацию по эл.почте
ACCOUNT_EMAIL_REQUIRED = True  # поле эл.почты не может быть пустой
ACCOUNT_UNIQUE_EMAIL = True  # поле эл.почты должно быть уникальным
ACCOUNT_USERNAME_REQUIRED = True  # поле username не обязательно
ACCOUNT_AUTHENTICATION_METHOD = "email"  # аутентификация по эл.почте
ACCOUNT_EMAIL_VERIFICATION = "optional"  # проверка эл.почты пока отключена
ACCOUNT_FORMS = {
    "signup": "newapp.models.BasicSignupForm"
}  # переназначается формы регистрации

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

# От django-apscheduler
# Строка формата для отображения временных меток времени выполнения на сайте администрирования Django.
# По умолчанию просто добавляет секунды к стандартному формату Django, что полезно для отображения
# временных меток для заданий, выполнение которых запланировано с интервалом менее одной минуты.
#
# См. https://docs.djangoproject.com/en/dev/ref/settings/#datetime-format для строки формата. Подробности синтаксиса.
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# От django-apscheduler
# Максимальное время выполнения, разрешенное для заданий, запускаемых вручную через сайт администрирования Django,
# что предотвращает истечение времени ожидания HTTP-запросов сайта администратора.
#
# Более длительные задания, вероятно, следует передать в библиотеку обработки фоновых задач.
# Который вместо этого поддерживает несколько фоновых рабочих процессов (например, Dramatiq, Celery, Django-RQ,
# и т. д. Популярные варианты см. на странице https://djangopackages.org/grids/g/workers-queues-tasks/).
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Секунды

# настройки Селери, подключение брокера
CELERY_BROKER_URL = "redis://localhost:6379"  # URL брокера сообщений (Redis)
CELERY_RESULT_BACKEND = (
    "redis://localhost:6379"  # хранилище результатов выполнения задач
)
CELERY_ACCEPT_CONTENT = ["application/json"]  # допустимый формат данных
CELERY_TASK_SERIALIZER = "json"  # метод сериализации задач
CELERY_RESULT_SERIALIZER = "json"  # метод сериализации результатов

# ведение журнала событий
LOGGING = {
    # версия настроек. насколько я понял настроек может быть несколько.
    "version": 1,
    # запускать ли остальные версии настроек
    "disable_existing_loggers": False,
    # стиль форматирования строк. в данном случае выбраны фигурные скобки, но дальше могут использоваться проценты.
    "style": "{",
    # настройка форматов отображения
    "formatters": {
        "verbose": {  # подробный формат
            # название уровня логирования, время создания,
            # идентификатор процесса, идентификатор процесса, сообщение
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",  # стиль форматирования строки
        },
        "simple_debug": {  # простой формат уровня отладки
            "format": "{asctime} {levelname} {message}",  # время, название уровня логирования и сообщение
            "style": "{",  # стиль форматирования строки
        },
        "simple_warning": {  # простой формат уровня "внимание!"
            # время, название уровня логирования, путь к источнику и сообщение
            "format": "{asctime} {levelname} {pathname} {message}",
            "style": "{",  # стиль форматирования строки
        },
        "simple_error": {  # простой формат уровня "ошибка"
            # время, название уровня логирования, путь к источнику, стек и сообщение
            "format": "{asctime} {levelname} {pathname} {exc_info} {message}",
            "style": "{",  # стиль форматирования строки
        },
        "general": {  # формат уровня "информационный"
            # время, название уровня логирования, название модуля и сообщение
            "format": "{asctime} {levelname} {module} {message}",
            "style": "{",  # стиль форматирования строки
        },
        "errors_by_email": {  # формат уровня "ошибок" для отправки на почту
            # время, название уровня логирования, путь к источнику и сообщение
            "format": "{asctime} {levelname} {pathname} {message}",
            "style": "{",  # стиль форматирования строки
        },
    },
    # фильтрация обработки
    "filters": {
        # пропускает сообщения когда включён режим отладки
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        # пропускает сообщения когда режим отладки выключен
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    # обработчики. что сделать с сообщением.
    "handlers": {
        # вывод в консоль
        "console_basic": {
            "level": "DEBUG",  # уровень отладки
            "filters": ["require_debug_true"],  # если включена отладка
            "class": "logging.StreamHandler",  # выводит в консоль
            "formatter": "simple_debug",  # формат для отладки
        },
        # вывод в консоль
        "console_warning": {
            "level": "WARNING",  # уровень предупреждения
            "filters": ["require_debug_true"],  # если включена отладка
            "class": "logging.StreamHandler",  # выводит в консоль
            "formatter": "simple_warning",  # формат для отладки
        },
        # вывод в консоль
        "console_error": {
            "level": "ERROR",  # уровень ошибки
            "filters": ["require_debug_true"],  # если включена отладка
            "class": "logging.StreamHandler",  # выводит в консоль
            "formatter": "simple_error",  # формат для отладки
        },
        # основная запись журнала в файл
        "general": {
            "level": "INFO",  # информационный уровень
            "filters": ["require_debug_false"],  # если отладка выключена
            "class": "logging.FileHandler",  # записывает в файл
            "filename": "logs/general.log",  # имя файла и путь к нему
            "formatter": "general",  # формат уровня
        },
        # запись журнала ошибок в файл
        "errors": {
            "level": "ERROR",  # уровень ошибки
            "class": "logging.FileHandler",  # записывает в файл
            "filename": "logs/errors.log",  # имя файла и путь к нему
            "formatter": "simple_error",  # формат уровня "ошибок"
        },
        # журнал безопасности
        "security": {
            "level": "DEBUG",  # уровень отладки
            "class": "logging.FileHandler",  # записывает в файл
            "filename": "logs/security.log",  # имя файла и путь к нему
            "formatter": "general",  # формат уровня
        },
        # отправка журнала на почту
        "mail_admins": {
            "level": "ERROR",  # уровень логирования
            "filters": ["require_debug_false"],  # если отладка выключена
            "class": "django.utils.log.AdminEmailHandler",  # отправляет сообщение на эл.почту администратору
            "formatter": "errors_by_email",  # формат уровня "ошибок" для отправки на почту
        },
    },
    # регистратор. первым получает сообщение и определяет куда его направить для обработки.
    "loggers": {
        # общего назначения
        "django": {
            # список обработчиков
            # в консоль, в файл
            "handlers": [
                "console_basic",
                "console_warning",
                "console_error",
                "general",
            ],
            "propagate": True,  # передавать запись в остальные уровни
        },
        # запросы
        "django.request": {
            # список обработчиков
            # в файл, по почте
            "handlers": ["errors", "mail_admins"],
            "propagate": True,  # передавать запись в остальные уровни
        },
        # сервер
        "django.server": {
            # список обработчиков
            # в файл
            "handlers": ["errors", "mail_admins"],
            "propagate": True,  # передавать запись в остальные уровни
        },
        # шаблоны
        "django.template": {
            # список обработчиков
            # в файл
            "handlers": ["errors"],
            "propagate": True,  # передавать запись в остальные уровни
        },
        # база данных
        "django.db.backends": {
            # список обработчиков
            # в файл
            "handlers": ["errors"],
            "propagate": True,  # передавать запись в остальные уровни
        },
        # безопасность
        "django.security": {
            # список обработчиков
            # в файл
            "handlers": ["security"],
            "propagate": True,  # передавать запись в остальные уровни
        },
    },
}
"""
что такое Логирование от "Диджитализируй":
https://dzen.ru/video/watch/623652b183d3092135b8f382?share_to=link в общих чертах о логировании.
от "Python Russian"
https://dzen.ru/video/watch/664c64d97645c414646bbb04?share_to=link как прописывать логи.
от "Андрей Иванов | Python":
https://youtu.be/nfml4BbBAbE?si=XYzoGGo1XaZmQIoP настройка Джанго.
Что нужно сделать по заданию:
https://disk.yandex.ru/i/wdjE4z10I6OOFA
как проверить работу логгера:
https://disk.yandex.ru/i/VU6B7kciMocseg
как настроить журнал. обучение от Джанго:
https://docs.djangoproject.com/en/5.1/howto/logging/#logging-how-to
Логгирование в Django (начальный обзор):
https://webdevblog.ru/loggirovanie-v-django-nachalnyj-obzor/
настройка отправки почты:
https://vivazzi.pro/ru/it/send-email-in-django/
https://tproger.ru/translations/email-functionality-django
"""

# Локализация и интернационализация
# путь к переводчику
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]
