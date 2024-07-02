from rest_framework import routers

from core.user.viewsets import UserViewSet
from core.actors.viewsets import ActorViewSet
from core.movies.viewsets import MovieViewSet
from core.awards.viewsets import AwardViewSet
from core.genres.viewsets import GenreViewSet
from core.cinemas.viewsets import CinemaViewSet
from core.directors.viewsets import DirectorViewSet
from core.languages.viewsets import LanguageViewSet
from core.reviews.viewsets import ReviewViewSet


router = routers.SimpleRouter()

# Routers provide an easy way of automatically determining the URL conf.
# User
router.register(r'users', UserViewSet, basename="users")
router.register(r'actors', ActorViewSet, basename="actors")
router.register(r'movies', MovieViewSet, basename="movies")
router.register(r'awards', AwardViewSet, basename="awards")
router.register(r'genres', GenreViewSet, basename="genres")
router.register(r'cinemas', CinemaViewSet, basename="cinemas")
router.register(r'directors', DirectorViewSet, basename="directors")
router.register(r'languages', LanguageViewSet, basename="languages")
router.register(r'reviews', ReviewViewSet, basename="reviews")


urlpatterns = [
    *router.urls
]
