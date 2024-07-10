from django.urls import path

from .views import ListOfAllNews, SpecificNews

urlpatterns = [
    path('', ListOfAllNews.as_view()),
    path('<int:pk>', SpecificNews.as_view()),
]
