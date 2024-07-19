from django_filters import FilterSet, ModelChoiceFilter

from .models import Post, Author


class ProductFilter(FilterSet):
    category_name_one_field = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор статьи или новости',
        empty_label='все'
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'date_creation': [
                'gt',
            ],
        }
