from django.urls import path

from .views import ListOfAllNews, SpecificNews, SearchByNews

urlpatterns = [
    path('', ListOfAllNews.as_view()),
    path('search/', SearchByNews.as_view()),
    path('<int:pk>', SpecificNews.as_view()),
]
