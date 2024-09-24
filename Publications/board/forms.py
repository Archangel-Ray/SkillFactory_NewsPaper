from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Publication


class PublicationForm(forms.ModelForm):
    content = forms.CharField(label="Содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Publication
        fields = [
            'title',
            'content',
            'category',
        ]
