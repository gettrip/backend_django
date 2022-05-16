from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, PlaceViewSet, RouteViewSet, UserViewSet, RoutePointViewSet, CityRoutesViewSet



router = DefaultRouter()
router.register(r'api/v1/users', UserViewSet)
router.register(r'api/v1/cities', CityViewSet)
router.register(r'api/v1/cities/(?P<city_id>[0-9]+)/routes', CityRoutesViewSet)
router.register(r'api/v1/places', PlaceViewSet)
router.register(r'api/v1/routes', RouteViewSet)
router.register(r'api/v1/routes/(?P<route_id>[0-9]+)/points', RoutePointViewSet)
urlpatterns = router.urls
