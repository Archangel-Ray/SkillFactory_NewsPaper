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


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
