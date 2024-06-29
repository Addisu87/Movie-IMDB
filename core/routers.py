from rest_framework import routers

from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()

# User
router.register(r'user', UserViewSet, basename="user")

# router.register(r'movies', MovieViewSet)
# router.register(r'ratings', RatingViewSet)
# router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    *router.urls
]
