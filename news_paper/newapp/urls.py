from django.urls import path

from .views import ListOfAllNews, SpecificNews, SearchByNews, NewsCreate

urlpatterns = [
    path('', ListOfAllNews.as_view(), name='список всех статей'),
    path('search/', SearchByNews.as_view(), name='поиск по всем статьям'),
    path('<int:pk>', SpecificNews.as_view(), name='вывод отдельной статьи'),
    path('create/', NewsCreate.as_view(), name='создание новости'),
    # path('<int:pk>/edit/', name='редактирование новости'),
    # path('<int:pk>/delete/', name='удаление новости'),
]
