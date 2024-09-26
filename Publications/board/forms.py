from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Publication, Comment


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
