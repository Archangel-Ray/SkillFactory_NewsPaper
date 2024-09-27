from django_filters import FilterSet

from .models import Comment


class SortByCategory(FilterSet):
    class Meta:
        model = Comment
        fields = {'publication'}
