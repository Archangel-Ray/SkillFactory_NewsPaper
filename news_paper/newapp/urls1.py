from django.urls import path

from .views import NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
    path("create/", NewsCreate.as_view(), name="создание новости"),
    path("<int:pk>/edit/", NewsUpdate.as_view(), name="редактирование новости"),
    path("<int:pk>/delete/", NewsDelete.as_view(), name="удаление новости"),
]
