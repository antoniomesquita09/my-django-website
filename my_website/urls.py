from django.urls import path
from django.urls import include
from django.contrib import admin
from MeuApp import views

urlpatterns = [
    # Define the namespace here
    path('MeuApp/', include('MeuApp.urls', namespace='MeuApp')),
    path('admin/', admin.site.urls),
    path("contatos/", include('contatos.urls')),
]
