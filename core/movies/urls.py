
from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('api/movies/', views.MovieList.as_view(), name="movie_list"),
    path('api/movies/<int:pk>/', views.MovieDetail.as_view(), name="movie_detail"),

    path('', include('core.reviews.urls')),

]
