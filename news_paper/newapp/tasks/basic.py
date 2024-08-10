from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

from newapp.models import Category, Post


def get_a_list_of_new_articles():
    for topic in Category.objects.all():
        a_week_earlier = datetime.now() - timedelta(days=7)
        a_week_earlier = timezone.make_aware(a_week_earlier, timezone=timezone.get_current_timezone())
        print(f'отправка рассылки на тему {topic}')
        list_posts = Post.objects.filter(post_category=topic, date_creation__gt=a_week_earlier)

        email_message = render_to_string(
            'mail/weekly_posts_distribution.html',
            {
                'by_category': topic,
                'posts': list_posts
            },
        )

        msg = EmailMultiAlternatives(
            subject=f'Посты за прошедшую неделю на тему {topic}',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email for user in topic.subscribers.all()],
        )
        msg.attach_alternative(email_message, "text/html")
        msg.send()
