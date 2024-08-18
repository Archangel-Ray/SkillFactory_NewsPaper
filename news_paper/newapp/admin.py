from django.contrib import admin

from .models import *


def set_category_article(modeladmin, request, queryset):
    queryset.update(category_type='AR')


def set_category_news(modeladmin, request, queryset):
    queryset.update(category_type='NW')


set_category_article.short_description = 'Установить статус "Статья"'
set_category_news.short_description = 'Установить статус "Новость"'


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'text', 'category_type', 'rating', 'date_creation', ]
    list_filter = ('author', 'rating', 'date_creation')
    search_fields = ('title', 'text')
    actions = [set_category_article, set_category_news]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_user', 'rating_author']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_subscribers']

    def get_subscribers(self, obj):
        return ", ".join([user.username for user in obj.subscribers.all()])

    get_subscribers.short_description = "Подписчики"


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
