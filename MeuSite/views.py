from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def homeSec(request):
    return render(request, "registro/homeSec.html")


def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
        context = {'form': formulario, }
        return render(request, 'registro/registro.html', context)

def paginaSecreta(request):
    return render(request, 'registro/paginaSecreta.html')