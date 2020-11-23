from django.db import models

# Create your models here.

class Planets(models.Model):

    def __str__(self):
        return self.item_noun

    planet_name = models.CharField(max_length=200)
    planet_size = models.CharField(max_length=200)
    planet_attributes = models.CharField(max_length=200)
    planet_location = models.CharField(max_length=200)