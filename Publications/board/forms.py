import random
from string import hexdigits

from allauth.account.forms import SignupForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.core.mail import send_mail

from Publications import settings
from .models import Publication, Comment


class CustomSignupForm(SignupForm):

    def save(self, request):
        # Убедитесь, что вы вызываете сохранение родительского класса.
        # .save() возвращает объект User.
        user = super(CustomSignupForm, self).save(request)

        # Добавьте сюда свою собственную обработку.
        user.is_active = False  # выключает активацию пользователя
        activation_code = ''.join(random.sample(hexdigits, 8))  # генерирует код из случайных букв и чисел
        user.last_name = activation_code  # записывает код в поле пользователя
        user.save()
        send_mail(
            subject=f'Код для активации аккаунта',
            message=f'Этот код {activation_code} нужно ввести в поле на сайте',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )

        # Вы должны вернуть исходный результат.
        return user


class PublicationForm(forms.ModelForm):
    content = forms.CharField(label="Содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Publication
        fields = [
            'title',
            'content',
            'category',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
