from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import PublicationForm
from .models import Publication


def main(request):
    return render(request, "basic.html")


class PublicationsList(ListView):
    model = Publication
    ordering = '-update_time'
    template_name = 'publications.html'
    context_object_name = 'publications'


class PublicationDetail(DetailView):
    model = Publication
    template_name = 'publication.html'
    context_object_name = 'publication'
    pk_url_kwarg = 'id'


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
