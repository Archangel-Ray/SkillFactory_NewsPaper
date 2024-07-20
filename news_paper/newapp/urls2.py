from django.urls import path

from .views import ListOfAllNews, SpecificNews, SearchByNews, NewsCreate, NewsUpdate, NewsDelete


urlpatterns = [
    path('create/', NewsCreate.as_view(), name='создание статьи'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='редактирование статьи'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='удаление статьи'),
]
