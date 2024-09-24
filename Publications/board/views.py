from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
