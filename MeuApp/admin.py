from django.contrib import admin

# Register your models here.
from MeuApp.models import Ride  # Make sure MeuApp is the correct app nam

admin.site.register(Ride)

