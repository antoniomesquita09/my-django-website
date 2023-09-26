from django.shortcuts import render


# Create your views here.

def home(request):
    # processamento antes de mostrar a home page
    return render(request, 'MeuApp/home.html')

def segunda(request):
    # processamento antes de mostrar a home page
    return render(request, 'MeuApp/segunda.html')
