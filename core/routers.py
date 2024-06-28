from core.user.viewsets import UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()

# User
router.register(r'users', UserViewSet, basename="users")

# router.register(r'movies', MovieViewSet)
# router.register(r'ratings', RatingViewSet)
# router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls
