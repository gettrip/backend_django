from django.db import models

# Create your models here.
class City(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    image = models.CharField(max_length=100, blank=False)
    