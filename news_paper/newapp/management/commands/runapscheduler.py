import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from newapp.tasks import get_a_list_of_new_articles

logger = logging.getLogger(__name__)


# def test_message_sending():
#     send_mail(
#         'Тестовая отправка сообщение из планировщика',
#         'Это сообщение пришло потому что я запустил планировщик на срабатывание каждые десять секунд',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=[settings.DEFAULT_FROM_EMAIL],
#     )


def weekly_newsletter():
    get_a_list_of_new_articles()


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # scheduler.add_job(
        #     test_message_sending,
        #     trigger=CronTrigger(second="*/10"),  # Every 10 seconds
        #     id="test_message_sending",  # Идентификатор, присвоенный каждому заданию, ДОЛЖЕН быть уникальным.
        #     max_instances=1,
        #     replace_existing=True,
        # )
        # logger.info("Added job 'test_message_sending'.")

        scheduler.add_job(
            weekly_newsletter,
            # trigger=CronTrigger(second="*/30"),
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Полночь понедельника, перед началом следующей рабочей недели.
            id="weekly_newsletter",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'weekly_newsletter'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
