import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_paper.settings')  # обновляет виртуальное окружение

app = Celery('news_paper')  # экземпляр Celery
app.config_from_object('django.conf:settings', namespace='CELERY')  # обновляет настройки экземпляра из текущих

app.autodiscover_tasks()  # ищет задачи


"""
запуск периодических задач на Windows в разных окнах терминала:
$ celery -A news_paper worker -l INFO --pool=solo
и
$ celery -A news_paper beat -l INFO
"""