from rest_framework import serializers

from .models import City, Place, Route, RoutePoint, User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('uid', 'username')


class CitySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = City
        fields = ('uid', 'name', 'image')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Place
        fields = ('uid', 'city_id', 'name', 'image', 'description', 'duration')


class RouteSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Route
        fields = ('uid', 'city_id', 'name', 'image', 'description', 'duration')


class RoutePointSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = RoutePoint
        fields = ('position', 'route_id', 'place_id', 'distance')
