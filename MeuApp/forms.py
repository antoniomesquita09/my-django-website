from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['destination', 'departure_time']

class JoinRideForm(forms.Form):
    user_name = forms.CharField(max_length=100)
