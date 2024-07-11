from django.views.generic import ListView, DetailView

from .models import Post


class ListOfAllNews(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'list_of_all_news.html'
    context_object_name = 'all_news'


class SpecificNews(DetailView):
    model = Post
    template_name = 'specific_news.html'
    context_object_name = 'specific_news'
