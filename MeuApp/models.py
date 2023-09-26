from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
