from django.urls import path

from .views import NewsCreate, NewsUpdate, NewsDelete, ListOfArticles, PostAPIUpdate

urlpatterns = [
    path("", ListOfArticles.as_view(), name="список всех статей"),
    path("<int:pk>", PostAPIUpdate.as_view(), name="api редактирование статьи"),
    path('create/', NewsCreate.as_view(), name='создание статьи'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='редактирование статьи'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='удаление статьи'),
]
