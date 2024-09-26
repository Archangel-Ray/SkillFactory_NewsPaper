from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = RichTextUploadingField(verbose_name="Содержание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('отдельная публикация', args=[str(self.id)])


class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='на публикацию')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Комментатор")
    content = models.TextField(verbose_name="Высказывание")
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
