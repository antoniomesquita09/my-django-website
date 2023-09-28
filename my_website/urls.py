from django.urls import path
from django.urls import include
from django.contrib import admin
from MeuApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contatos', include('contatos.urls')),
    path('rides/', views.ride_list, name='ride_list'),
    path('admin/', admin.site.urls)
]
