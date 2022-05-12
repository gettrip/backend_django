from rest_framework.routers import DefaultRouter
from .views import CityViewSet, PlaceViewSet, RouteViewSet


router = DefaultRouter()
router.register(r'api/v1/cities', CityViewSet)
router.register(r'api/v1/places', PlaceViewSet)
router.register(r'api/v1/routes', RouteViewSet)
urlpatterns = router.urls