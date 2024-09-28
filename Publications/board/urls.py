from django.urls import path

from .views import PublicationsList, PublicationDetail, PublicationCreate, PublicationEdit, ResponsesToMyPublications

urlpatterns = [
    path("", PublicationsList.as_view(), name='основная страница'),
    path("<int:pk>/", PublicationDetail.as_view(), name='отдельная публикация'),
    path("create/", PublicationCreate.as_view(), name='создать публикацию'),
    path("<int:id>/edit/", PublicationEdit.as_view(), name='изменить публикацию'),
    path('private/', ResponsesToMyPublications.as_view(), name='посмотреть отклики'),
]
