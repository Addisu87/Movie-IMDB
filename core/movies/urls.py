
from django.urls import path, include
from .views import MovieList, MovieDetail

app_name = 'movies'

urlpatterns = [
    path('movies/', MovieList.as_view(), name="movie_list"),
    path('movies/<int:pk>/', MovieDetail.as_view(), name="movie_detail"),
]
