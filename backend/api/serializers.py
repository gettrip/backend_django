from rest_framework import serializers
from .models import City, Place, Route

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'image')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'city_id', 'name', 'image', 'description', 'duration')   


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'city_id', 'name', 'image', 'description', 'duration')  
    