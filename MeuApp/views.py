from http.client import HTTPResponse
from .models import Ride  # Import the Ride model
from .forms import RideForm, JoinRideForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.views.generic import ListView
from django.http import HttpResponseBadRequest
from .models import Ride, Profile
from .forms import RideForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Point to your custom template if needed
    redirect_authenticated_user = True  # If True, authenticated users will be redirected to LOGIN_REDIRECT_URL
    # Add more customization if needed

class CustomLogoutView(LogoutView):
    next_page = 'MeuApp/home'  # Replace with your URL name

def ride_list(request):
    rides = Ride.objects.all()
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MeuApp: ride_list')
    else:
        form = RideForm()
    return render(request, 'MeuApp/ride_list.html', {'rides': rides, 'form': form})

def home(request):
    # processamento antes de mostrar a home page
    return render(request, 'MeuApp/home.html')


class RideListView(ListView):
    model = Ride
    template_name = 'ride_list.html'  # Adjust this to your actual template name
    context_object_name = 'rides'



@login_required
def add_ride(request):
    if not hasattr(request.user, 'profile'):
        # This will raise an error if the user doesn't have a profile
        return HTTPResponse("User has no associated profile.", status=400)

    if request.method == "POST":
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.driver = request.user.profile
            ride.save()
            return redirect('MeuApp:ride_list')  # Redirect to home view after successful submission
    else:
        form = RideForm()
    return render(request, 'MeuApp/add_ride.html', {'form': form})

@login_required
def join_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    if ride.free_seats > 0:
        ride.passengers.add(request.user.profile)
        ride.free_seats -= 1
        ride.save()
        return redirect('MeuApp:ride_list')
    else:
        return HttpResponseBadRequest("No free seats available")

# ... rest of your views

