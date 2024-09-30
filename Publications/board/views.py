from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin

from Publications import settings
from .filters import FilterByPublications
from .forms import PublicationForm, CommentForm
from .models import Publication, Comment


def main(request):
    return render(request, "basic.html")


class PublicationsList(ListView):
    model = Publication
    ordering = '-update_time'
    template_name = 'publications.html'
    context_object_name = 'publications'


class PublicationDetail(FormMixin, DetailView):
    model = Publication
    template_name = 'publication.html'
    context_object_name = 'publication'
    pk_url_kwarg = 'pk'
    form_class = CommentForm
    """
    добавил форму для добавления комментария так как показано здесь:
    https://www.thecoderscamp.com/django-implementing-a-form-within-a-generic-detailviewdjango/
    """

    def get_success_url(self):
        return reverse('отдельная публикация', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PublicationDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['responses'] = Comment.objects.all().filter(publication=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.publication = self.object
        comment.user = self.request.user
        form.save()

        message = f'Вы получили отклик на публикацию: "{self.object}"'
        author = comment.publication.user
        send_mail(
            subject='Поступил новый отклик',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[author.email, ]
        )
        return super(PublicationDetail, self).form_valid(form)


class PublicationCreate(LoginRequiredMixin, CreateView):
    form_class = PublicationForm
    model = Publication
    template_name = 'publication_editing.html'

    def form_valid(self, form):
        publication = form.save(commit=False)
        publication.user = self.request.user
        return super().form_valid(form)


class PublicationEdit(LoginRequiredMixin, UpdateView):
    form_class = PublicationForm
    model = Publication
    template_name = 'publication_editing.html'
    pk_url_kwarg = 'id'
    context_object_name = 'publication'


class ResponsesToMyPublications(ListView):
    model = Comment
    template_name = "response_list.html"
    context_object_name = "responses"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication__user__id=self.request.user.id)
        self.filterset = FilterByPublications(self.request.GET, queryset, request=self.request.user.id)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filterset"] = self.filterset
        return context


def accept_the_response(request, pk):
    Comment.objects.filter(id=pk).update(status=True)
    response = Comment.objects.get(id=pk)
    author_of_the_response = response.user
    message = f'Ваш отклик на публикацию "{response.publication.title}" был принят автором. Вы можете его увидеть.'
    send_mail(
        subject='Отклик принят',
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[author_of_the_response.email]
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_response(request, pk):
    response = Comment.objects.get(id=pk)
    response.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
