from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


def set_category_article(modeladmin, request, queryset):
    queryset.update(category_type='AR')


def set_category_news(modeladmin, request, queryset):
    queryset.update(category_type='NW')


set_category_article.short_description = 'Установить статус "Статья"'
set_category_news.short_description = 'Установить статус "Новость"'


class PostAdmin(TranslationAdmin, admin.ModelAdmin):
    model = Post
    list_display = ['title', 'author', 'get_post_text', 'category_type', 'rating', 'date_creation', ]
    list_filter = ('author', 'rating', 'date_creation')
    search_fields = ('title', 'text')
    actions = [set_category_article, set_category_news]

    def get_post_text(self, obj):
        if len(obj.text) >= 50:
            return f'{obj.text[:50]} ...'
        return obj.text

    get_post_text.short_description = "Текст поста"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_user', 'rating_author']


class CategoryAdmin(TranslationAdmin, admin.ModelAdmin):
    model = Category
    list_display = ['name', 'get_subscribers']

    def get_subscribers(self, obj):
        return ", ".join([user.username for user in obj.subscribers.all()])

    get_subscribers.short_description = "Подписчики"


class CommentAdmin(TranslationAdmin, admin.ModelAdmin):
    model = Comment
    list_display = ['get_title_post', 'comment_user', 'get_comment_text', 'date_creation', 'rating',
                    'get_author_of_post']
    list_filter = ['comment_user']
    search_fields = ['text']

    def get_title_post(self, obj):
        return f'{obj.comment_post.title}'

    def get_comment_text(self, obj):
        if len(obj.text) >= 50:
            return f'{obj.text[:50]} ...'
        return obj.text

    get_title_post.short_description = "Название поста"
    get_comment_text.short_description = "Текст сообщения"


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
