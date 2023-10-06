from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View

from .forms import RideModel2Form
from django.shortcuts import render, get_object_or_404


class RideCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {'formulario': RideModel2Form}
        return render(request, 'MeuApp/criaCarona.html', context)

    def post(self, request, *args, **kwargs):
        formulario = RideModel2Form(request.POST)
        print('enter')
        if formulario.is_valid():
            print('Form valid')
            print(formulario.fields)
            ride = formulario.save()
            print(ride)
            # ride.save()
            return HttpResponseRedirect(reverse_lazy('MeuApp:cria-carona'))
