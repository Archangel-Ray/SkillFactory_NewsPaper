from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    ListOfAllNews,
    SpecificNews,
    SearchByNews,
    NewsCreate,
    NewsUpdate,
    NewsDelete,
    ProductsByCategory,
    subscribe,
    unsubscribe,
)

urlpatterns = [
    path("", ListOfAllNews.as_view(), name="список всех постов"),
    path("search/", SearchByNews.as_view(), name="поиск по всем постам"),
    path(
        "<int:pk>",
        cache_page(60)(SpecificNews.as_view()),
        name="вывод отдельного поста",
    ),
    path("create/", NewsCreate.as_view(), name="создание новости"),
    path("<int:pk>/edit/", NewsUpdate.as_view(), name="редактирование новости"),
    path("<int:pk>/delete/", NewsDelete.as_view(), name="удаление новости"),
    path("category/<int:pk>", ProductsByCategory.as_view(), name="товары по категории"),
    path("category/<int:pk>/subscribe", subscribe, name="подписка на категорию"),
    path("category/<int:pk>/unsubscribe", unsubscribe, name="отписаться от категории"),
]
