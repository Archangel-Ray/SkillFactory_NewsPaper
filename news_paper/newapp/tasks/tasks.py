from datetime import timedelta, datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import gettext

from newapp.models import Post, PostCategory, Category


@shared_task
def message_about_create_a_new_post(post_id):
    new_post = Post.objects.get(id=post_id)
    new_post_category = PostCategory.objects.get(
        post_through=new_post.id
    ).category_through
    email_message = render_to_string(
        "mail/message_about_new_post.html",
        {
            "by_category": new_post_category,
            "post": new_post,
        },
    )

    msg = EmailMultiAlternatives(
        subject=new_post.title,
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email for user in new_post_category.subscribers.all()],
    )
    msg.attach_alternative(email_message, "text/html")
    msg.send()


@shared_task
def get_a_list_of_new_articles():
    for topic in Category.objects.all():
        a_week_earlier = datetime.now() - timedelta(days=7)
        a_week_earlier = timezone.make_aware(
            a_week_earlier, timezone=timezone.get_current_timezone()
        )
        list_posts = Post.objects.filter(
            post_category=topic, date_creation__gt=a_week_earlier
        )

        email_message = render_to_string(
            "mail/weekly_posts_distribution.html",
            {"by_category": topic, "posts": list_posts},
        )

        msg = EmailMultiAlternatives(
            subject=f"{gettext('Посты за прошедшую неделю на тему')} {topic}",
            body="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email for user in topic.subscribers.all()],
        )
        msg.attach_alternative(email_message, "text/html")
        msg.send()


"""
запуск периодических задач на Windows в разных окнах терминала:
$ celery -A news_paper worker -l INFO --pool=solo
и
$ celery -A news_paper beat -l INFO
"""
