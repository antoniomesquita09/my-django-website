from .models import Ride  # Import the Ride model
from .forms import RideForm
from django.shortcuts import render, redirect


def ride_list(request):
    rides = Ride.objects.all()
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ride_list')
    else:
        form = RideForm()
    return render(request, 'MeuApp/ride_list.html', {'rides': rides, 'form': form})

def home(request):
    # processamento antes de mostrar a home page
    return render(request, 'MeuApp/home.html')

def segunda(request):
    # processamento antes de mostrar a home page
    return render(request, 'MeuApp/segunda.html')

def add_ride(request):
    if request.method == "POST":
        form = RideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ride_list')  # Redirect to ride list view after successful submission
    else:
        form = RideForm()
    return render(request, 'MeuApp/add_ride.html', {'form': form})
from django.shortcuts import get_object_or_404, redirect
from .models import Ride

def join_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    if ride.free_seats > 0:
        ride.free_seats -= 1
        ride.save()
    return redirect('ride_list')  # adjust the name of your ride list view

# def ride_list(request):
#     rides = Ride.objects.all()  # Fetch all rides
#     return render(request, 'MeuApp/ride_list.html', {'rides': rides})