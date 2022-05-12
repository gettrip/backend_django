from django.db import models


class City(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    image = models.CharField(max_length=100, blank=False)
    

class Place(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    city_id = models.ForeignKey(City, blank=False, null=True, on_delete=models.SET_NULL)
    image = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    duration = models.PositiveIntegerField()


class Route(models.Model):    
    name = models.CharField(max_length=200, blank=False, unique=True)
    city_id = models.ForeignKey(City, blank=False, null=True, on_delete=models.SET_NULL)
    image = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    places = models.ManyToManyField(Place)

    models.UniqueConstraint(fields=[name, city_id], name='unique_city_route')
