from django.urls import path

from .views import ListOfAllNews, SpecificNews, SearchByNews, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
    path('', ListOfAllNews.as_view(), name='список всех статей'),
    path('search/', SearchByNews.as_view(), name='поиск по всем статьям'),
    path('<int:pk>', SpecificNews.as_view(), name='вывод отдельной статьи'),
    path('create/', NewsCreate.as_view(), name='создание новости'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='редактирование новости'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='удаление новости'),
    path('articles/create/', NewsCreate.as_view(), name='создание статьи'),
    path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='редактирование статьи'),
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='удаление статьи'),
]
