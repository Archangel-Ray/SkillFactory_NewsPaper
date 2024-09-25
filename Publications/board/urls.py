from django.urls import path

from .views import PublicationsList, PublicationDetail, PublicationCreate

urlpatterns = [
    path("", PublicationsList.as_view(), name='основная страница'),
    path("<int:id>/", PublicationDetail.as_view(), name='publication_detail'),
    path("create/", PublicationCreate.as_view(), name='создать публикацию'),
]
