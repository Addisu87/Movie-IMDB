from rest_framework import generics
from rest_framework.exceptions import ValidationError

from core.reviews.models import Review
from core.reviews.serializers import ReviewSerializer
from core.movies.models import Movie

# using generic class-based views


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)

        review_user = self.request.user
        review_query = Review.objects.filter(movie=movie, user=review_user)

        if review_query.exists():
            raise ValidationError("You have already reviewed this movie.")
        serializer.save(movie=movie, user=review_user)


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
