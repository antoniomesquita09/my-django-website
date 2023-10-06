from django.contrib.auth.models import User
from django.db import models


class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_driver')
    passengers = models.ManyToManyField(User, related_name='rides_as_passenger', blank=True)
    destination = models.CharField(max_length=255)
    departure_time = models.TimeField()
    free_seats = models.PositiveIntegerField(default=3)  # Adjust default as per your needs

