import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "news_paper.settings"
)  # обновляет виртуальное окружение

app = Celery("news_paper")  # экземпляр Celery
app.config_from_object(
    "django.conf:settings", namespace="CELERY"
)  # обновляет настройки экземпляра из текущих

app.autodiscover_tasks()  # ищет задачи

app.conf.beat_schedule = {
    "отправка сообщение о новом посте": {  # периодическая задача
        "task": "newapp.tasks.tasks.message_about_create_a_new_post",  # задача которая должна выполняться
        "args": ("post_id",),
    },
}

app.conf.beat_schedule = {
    "еженедельная рассылка по тематикам": {
        "task": "newapp.tasks.tasks.get_a_list_of_new_articles",
        "schedule": crontab(hour="8", minute="0", day_of_week="monday"),
    }
}

"""
запуск периодических задач на Windows в разных окнах терминала:
$ celery -A news_paper worker -l INFO --pool=solo
и
$ celery -A news_paper beat -l INFO
"""
