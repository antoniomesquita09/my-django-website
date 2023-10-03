from django.contrib.auth.views import LoginView
from django.urls import path
from django.urls import include
from django.contrib import admin

from MeuSite import views

urlpatterns = [
    # Define the namespace here
    path('MeuApp/', include('MeuApp.urls', namespace='MeuApp')),
    path('admin/', admin.site.urls),
    path("contatos/", include('contatos.urls')),
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro/', views.registro, name='sec-registro'),
    path('accounts/login/', LoginView.as_view(template_name='registro/login.html'), name='sec-login'),
    path('accounts/profile/', views.paginaSecreta, name='sec-paginaSecreta')
]
