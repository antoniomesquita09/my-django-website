from django.urls import path
from django.urls import include
from django.contrib import admin
from MeuApp import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('/segunda', views.segunda, name="segunda"),
    path('/contatos', include('contatos.urls')),
    path('admin/', admin.site.urls)
]
