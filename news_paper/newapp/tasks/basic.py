from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


def signal_to_create_a_new_post(instance):
    for category in instance.post_category.all():
        email_message = render_to_string(
            'mail/message_about_new_post.html',
            {
                'by_category': category,
                'post': instance
            },
        )

        msg = EmailMultiAlternatives(
            subject=instance.title,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email for user in category.subscribers.all()],
        )
        msg.attach_alternative(email_message, "text/html")
        msg.send()
