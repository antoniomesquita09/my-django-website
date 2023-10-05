from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View

from .models import Ride  # Import the Ride model
from .forms import RideModel2Form, JoinRideForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView


@login_required
def ride_list(request):
    rides = Ride.objects.all()
    if request.method == 'POST':
        form = RideModel2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ride_list')
    else:
        form = RideModel2Form()
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
    if request.method == 'POST':
        form = RideModel2Form(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)

            # Access username through the user field of the Profile model
            driver_name = ride.driver.user.username if ride.driver else "Anonymous"
            # if passengers is a ManyToManyField with Profile, you need to add the driver to it.

            ride.save()
            if ride.driver:  # Checking if driver is not None
                ride.passengers.add(ride.driver)  # Adding the driver to the passengers

            return redirect('MeuApp:ride_list')
    else:
        form = RideModel2Form()
    return render(request, 'MeuApp/add_ride.html', {'form': form})


# def ride_list(request):
#     rides = Ride.objects.all()  # Fetch all rides
#     return render(request, 'MeuApp/ride_list.html', {'rides': rides})
@login_required
def join_ride(request, ride_id):  # assuming you are passing ride_id to this view to identify the ride
    ride = get_object_or_404(Ride, id=ride_id)
    if request.method == 'POST':
        form = JoinRideForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']

            # Append this username to the passengers list of the ride
            ride.passengers = f"{ride.passengers},{user_name}" if ride.passengers else user_name
            ride.save()

            return redirect('MeuApp:ride_list')  # or redirect to any appropriate URL
    else:
        form = JoinRideForm()
    return render(request, 'MeuApp/join_ride.html', {'form': form, 'ride': ride})


class RideCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {'formulario': RideModel2Form(initial=Ride.driver)}
        return render(request, 'MeuApp/criaCarona.html', context)

    def post(self, request, *args, **kwargs):
        formulario = RideModel2Form(request.POST)
        print(formulario.save())
        if formulario.is_valid():
            ride = formulario.save()
            print(ride)
            ride.driver_id = request.user.id
            ride.save()
            return HttpResponseRedirect(reverse_lazy('MeuApp:ride_list'))
