from django.urls import path

from .views import PublicationsList

urlpatterns = [
    path("", PublicationsList.as_view(), name='основная страница'),
]
