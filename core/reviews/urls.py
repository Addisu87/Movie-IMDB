
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('api/reviews/', views.ReviewList.as_view(), name="review_list"),
    path('api/reviews/<int:pk>/',
         views.ReviewDetail.as_view(), name="review_detail"),
]
