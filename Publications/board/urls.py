from django.urls import path

from .views import PublicationsList, PublicationDetail

urlpatterns = [
    path("", PublicationsList.as_view(), name='основная страница'),
    path("<int:id>/", PublicationDetail.as_view(), name='публикация'),
]
