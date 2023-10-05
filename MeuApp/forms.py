# MeuApp/forms.py
from django import forms
from .models import Ride


class RideModel2Form(forms.ModelForm):
    departure_time = forms.TimeField(
        help_text='Horario de saida no formato hh:mm',
        input_formats=['%H:%M'],
        label='Horario de saida',
        required=True
    )
    destination = forms.CharField(
        help_text='Local de destino',
        label='Local de destino',
        required=True
    )
    free_seats = forms.IntegerField(
        help_text='Quantidade de vagas',
        label='Quantidade de vagas',
        max_value=4,
        min_value=1,
        required=True,
    )
    # passengers = models.ManyToManyField(Profile, related_name='rides_as_passenger', blank=True)
    # destination = models.CharField(max_length=255)
    # departure_time = models.TimeField()
    # free_seats = models.PositiveIntegerField(default=3)  # Adjust default as per your needs

    class Meta:
        model = Ride
        fields = ['departure_time', 'destination', 'free_seats']


class JoinRideForm(forms.Form):
    user_name = forms.CharField(max_length=100)
