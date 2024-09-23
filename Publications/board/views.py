from django.shortcuts import render
from django.views.generic import ListView

from .models import Publication


def main(request):
    return render(request, "basic.html")


class PublicationsList(ListView):
    model = Publication
    ordering = '-update_time'
    template_name = 'publications.html'
    context_object_name = 'publications'
