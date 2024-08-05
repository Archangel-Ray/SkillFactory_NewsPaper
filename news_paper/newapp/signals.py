from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import PostCategory
from .tasks import signal_to_create_a_new_post


@receiver(m2m_changed, sender=PostCategory)
def sending_notification_about_a_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        signal_to_create_a_new_post(instance)
