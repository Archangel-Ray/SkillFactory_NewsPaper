from django import forms
from django.utils.translation import gettext
from django_filters import FilterSet, ModelChoiceFilter, DateFilter

from .models import Post, Author


class ProductFilter(FilterSet):
    category_name_one_field = ModelChoiceFilter(
        field_name="author",
        queryset=Author.objects.all(),
        label=gettext("Автор статьи или новости"),
        empty_label=gettext("все"),
    )

    more_than_this_date = DateFilter(
        widget=forms.DateInput(attrs={"type": "date"}),
        lookup_expr="date__gte",
        field_name="date_creation",
    )

    class Meta:
        model = Post
        fields = {
            "title": ["icontains"],
        }
