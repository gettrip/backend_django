from rest_framework.routers import DefaultRouter

from .views import (CityRoutesViewSet, CityViewSet, PlaceViewSet, RoutePointViewSet,
                    RouteViewSet, UserViewSet)

router = DefaultRouter()
router.register('api/v1/users', UserViewSet)
router.register('api/v1/cities', CityViewSet)
router.register('api/v1/cities/(?P<city_id>[0-9]+)/routes', CityRoutesViewSet)
router.register('api/v1/places', PlaceViewSet)
router.register('api/v1/routes', RouteViewSet)
router.register('api/v1/routes/(?P<route_id>[0-9]+)/points', RoutePointViewSet)
urlpatterns = router.urls
