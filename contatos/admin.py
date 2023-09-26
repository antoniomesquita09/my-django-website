from django.contrib import admin
from contatos.models import Pessoa
from MeuApp.models import Ride  # Make sure MeuApp is the correct app name

admin.site.register(Pessoa)
admin.site.register(Ride)
