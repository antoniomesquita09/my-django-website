from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='Enter the driver name')
    age = models.IntegerField(help_text='Enter the age')
    email = models.EmailField(help_text='Enter the email', max_length=254)
    phone = models.CharField(help_text='Phone with country and area code', max_length=20)
    vehicle_model = models.CharField(max_length=100, help_text='Enter the vehicle model')
    vehicle_number = models.CharField(max_length=20, help_text='Enter the vehicle number')
    available_seats = models.IntegerField(help_text='Enter the number of available seats')
    destination = models.CharField(max_length=100, help_text='Enter the destination')
    departure_time = models.DateTimeField(help_text='Enter the departure time')
    is_available = models.BooleanField(default=True, help_text='Is the driver available for a ride?')

    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional fields can be added here
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

# create or update user profile automatically when creating or updating a user
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Ride(models.Model):
    driver = models.ForeignKey('MeuApp.Profile', on_delete=models.CASCADE, related_name='rides_as_driver')
    passenger = models.ForeignKey('MeuApp.Profile', on_delete=models.CASCADE, related_name='rides_as_passenger')
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    
    class Meta:
        ordering = ['departure_time']
        permissions = [('can_give_ride', 'Can give a ride')]
        default_permissions = ('add', 'change', 'delete', 'view')
