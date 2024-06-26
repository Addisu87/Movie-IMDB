
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('review/', views.ReviewList.as_view(), name="review_list"),
    path('review/<int:pk>/',
         views.ReviewDetail.as_view(), name="review_detail"),
]
