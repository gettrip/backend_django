from .models import City, Place, Route, User, RoutePoint
from .serializers import CitySerializer, PlaceSerializer, RouteSerializer, UserSerializer, RoutePointSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class CityRoutesViewSet(RouteViewSet):    
    def get_queryset(self):        
        city_id = self.kwargs['city_id']               
        return Route.objects.filter(city_id=city_id)        

class RoutePointViewSet(viewsets.ModelViewSet):
    queryset = RoutePoint.objects.all()    
    serializer_class = RoutePointSerializer

    def get_queryset(self):
        route_id = self.kwargs['route_id']        
        return RoutePoint.objects.filter(route_id=route_id)
