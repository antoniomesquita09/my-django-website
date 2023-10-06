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

    class Meta:
        model = Ride
        fields = '__all__'
