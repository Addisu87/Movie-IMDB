
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('movies/<int:pk>/reviews/',
         views.ReviewList.as_view(), name="review_list"),
    path('movies/<int:pk>/create_reviews/',
         views.ReviewCreate.as_view(), name="review_create"),
    path('movies/reviews/<int:pk>/',
         views.ReviewDetail.as_view(), name="review_detail"),
]
