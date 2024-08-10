from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from newapp.models import Post, PostCategory


@shared_task
def message_about_create_a_new_post(post_id):
    new_post = Post.objects.get(id=post_id)
    new_post_category = PostCategory.objects.get(post_through=new_post.id).category_through
    email_message = render_to_string(
        'mail/message_about_new_post.html',
        {
            'by_category': new_post_category,
            'post': new_post,
        },
    )

    msg = EmailMultiAlternatives(
        subject=new_post.title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email for user in new_post_category.subscribers.all()],
    )
    msg.attach_alternative(email_message, "text/html")
    msg.send()
