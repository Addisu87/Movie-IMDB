from rest_framework import routers

from core.user.viewsets import UserViewSet
from core.actors.viewsets import ActorViewSet
from core.directors.viewsets import DirectorViewSet
from core.movies.viewsets import MovieViewSet
from core.reviews.viewsets import ReviewViewSet
from core.auth.viewsets.register import RegisterViewSet


router = routers.SimpleRouter()

# Routers provide an easy way of automatically determining the URL conf.
#################### USER ####################
router.register(r'users', UserViewSet, basename="users")

router.register(r'movies', MovieViewSet, basename="movies")
router.register(r'actors', ActorViewSet, basename="actors")
router.register(r'directors', DirectorViewSet, basename="directors")
router.register(r'reviews', ReviewViewSet, basename="reviews")

#################### AUTH ####################
router.register(r'auth/register', RegisterViewSet, basename="auth-register")

urlpatterns = [
    *router.urls
]
