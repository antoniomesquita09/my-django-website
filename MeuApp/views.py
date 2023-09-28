from django.shortcuts import render
from .models import Ride  # Import the Ride model




# Create your views here.

def home(request):
    # processamento antes de mostrar a home page
    return render(request, 'MeuApp/home.html')

def segunda(request):
    # processamento antes de mostrar a home page
    return render(request, 'MeuApp/segunda.html')

def ride_list(request):
    rides = Ride.objects.all()  # Fetch all rides
    return render(request, 'MeuApp/ride_list.html', {'rides': rides})