from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_size = models.CharField(max_length=200)
    item_mass = models.CharField(max_length=200, default="default")
    item_age = models.CharField(max_length=200, default = "default")
    item_characteristics = models.CharField(max_length=500)
    item_distance = models.CharField(max_length=200)
    background_image = models.CharField(max_length=500, default='https://i0.wp.com/dotsandlines.steveboerner.com/wp-content/uploads/2016/06/earth_planet_600x300.jpg?resize=600%2C400')


    def get_absolute_url(self):
        return reverse("SolarModel:detail", kwargs={"pk": self.pk})