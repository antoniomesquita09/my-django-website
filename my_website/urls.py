from django.urls import path
from django.urls import include
from django.contrib import admin
from MeuApp import views

urlpatterns = [
    path('MeuApp/', include('MeuApp.urls', namespace='MeuApp')), # Define the namespace here
    path('admin/', admin.site.urls),


]
