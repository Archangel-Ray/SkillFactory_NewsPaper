from modeltranslation.translator import register, TranslationOptions

from .models import Author, Category, Post, Comment


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text',)
