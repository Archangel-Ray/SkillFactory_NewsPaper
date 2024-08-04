from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from newapp.filters import ProductFilter
from newapp.forms import PostForm
from .models import Post, Category


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


class NewsCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_editing.html'
    permission_required = ('newapp.add_post',)

    def form_valid(self, form):
        new_post = form.save(commit=False)
        if 'news' in self.request.path:
            new_post.category_type = 'NW'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_editing.html'
    permission_required = ('newapp.change_post',)


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_deleting.html'
    success_url = reverse_lazy('список всех постов')


class ProductsByCategory(ListOfAllNews):
    model = Post
    template_name = 'list_of_news_by_category.html'
    context_object_name = 'list_by_category'

    def get_queryset(self):
        """
        Фильтрует новости по полученной категории
        """
        self.by_category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(post_category=self.by_category).order_by('-date_creation')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Получает статус пользователя по текущей категории
        """
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.by_category.subscribers.all()
        context['by_category'] = self.by_category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if not category.subscribers.filter(id=user.id).exists():
        category.subscribers.add(user)

        message = 'Вы подписались на рассылку новостей по теме'

        email_message = render_to_string(
            'mail/successful_subscription.html',
            {
                'by_category': category,
                'name': user.username,
            },
        )

        msg = EmailMultiAlternatives(
            subject=f'Подписка на тему: {category}',
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        msg.attach_alternative(email_message, "text/html")
        msg.send()

    else:
        message = 'Вы уже подписаны на тему'

    return render(request, 'subscribe.html', {'category': category, 'message': message})


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if category.subscribers.filter(id=user.id).exists():
        category.subscribers.remove(user)

        message = 'Отключена подписка на рассылку по теме'

        email_message = render_to_string(
            'mail/subscription_cancellation_message.html',
            {
                'by_category': category,
                'name': user.username,
            },
        )

        msg = EmailMultiAlternatives(
            subject=f'Прекращена подписка на тему: {category}',
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        msg.attach_alternative(email_message, "text/html")
        msg.send()
    else:
        message = 'Не получается.\nВозможно, Вы не были подписаны на тему'
    return render(request, 'subscribe.html', {'category': category, 'message': message})
