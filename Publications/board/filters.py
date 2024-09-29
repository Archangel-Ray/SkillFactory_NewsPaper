from django_filters import FilterSet

from .models import Comment, Publication


class FilterByPublications(FilterSet):
    class Meta:
        model = Comment
        fields = {'publication'}

    def __init__(self, *args, **kwargs):
        super(FilterByPublications, self).__init__(*args, **kwargs)
        self.filters['publication'].queryset = Publication.objects.filter(user_id=kwargs['request'])
