from django.views.generic import ListView, DetailView, CreateView, UpdateView

from newapp.filters import ProductFilter
from newapp.forms import PostForm
from .models import Post


class ListOfAllNews(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'list_of_all_news.html'
    context_object_name = 'all_news'
    paginate_by = 10


class SearchByNews(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'search_news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class SpecificNews(DetailView):
    model = Post
    template_name = 'specific_news.html'
    context_object_name = 'specific_news'


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_editing.html'

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.category_type = 'NW'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_editing.html'
