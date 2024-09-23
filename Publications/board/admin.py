from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms

from .models import Category, Publication

admin.site.register(Category)


# форма СК-редактора
class PublicationAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Содержимое")

    class Meta:
        model = Publication
        fields = '__all__'


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    form = PublicationAdminForm
