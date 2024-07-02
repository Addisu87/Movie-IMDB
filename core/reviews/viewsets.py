from rest_framework.exceptions import ValidationError

from core.abstract.viewsets import AbstractViewSet
from core.reviews.models import Review
from core.reviews.serializers import ReviewSerializer
from core.movies.models import Movie


class ReviewViewSet(AbstractViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)

        reviewer = self.request.user
        review_query = Review.objects.filter(movie=movie, user=reviewer)

        if review_query.exists():
            raise ValidationError("You have already reviewed this movie.")
        serializer.save(movie=movie, user=reviewer)
