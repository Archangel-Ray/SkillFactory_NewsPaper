from django_filters import FilterSet

from .models import Comment


class FilterByPublications(FilterSet):
    class Meta:
        model = Comment
        fields = {'publication'}
