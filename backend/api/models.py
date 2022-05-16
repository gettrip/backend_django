from django.db import models


class User(models.Model):        
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)


class City(models.Model):   
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=100)
    

class Place(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, db_column='city_id')
    image = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField() 

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'city_id'], name='unique_city_place')]


class Route(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, db_column='city_id')
    image = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'city_id'], name='unique_city_route')]


class RoutePoint(models.Model):
    position = models.PositiveIntegerField(blank=False)
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    distance = models.PositiveIntegerField(blank=False)    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['place_id', 'route_id'], name='unique_routepoint'),
            models.UniqueConstraint(fields=['position', 'route_id'], name='unique_position')
        ]
