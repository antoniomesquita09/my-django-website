from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy
from django.urls import include
from django.contrib import admin
from django.views.generic import UpdateView

from MeuSite import views

urlpatterns = [
    # Define the namespace here
    path('MeuApp/', include('MeuApp.urls', namespace='MeuApp')),
    path('admin/', admin.site.urls),
    path("contatos/", include('contatos.urls')),
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro/', views.registro, name='sec-registro'),
    path('accounts/login/', LoginView.as_view(template_name='registro/login.html'), name='sec-login'),
    path('accounts/profile/', views.paginaSecreta, name='sec-paginaSecreta'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home')), name='sec-logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(
        template_name='registro/password_change_form.html',
        success_url=reverse_lazy('sec-password_change_done'),
    ), name='sec-password_change'),
    path('accounts/password_change_done/', PasswordChangeDoneView.as_view(
        template_name='registro/password_change_done.html'
    ), name='sec-password_change_done'),
    path('accounts/terminaRegistro/<int:pk>/',
         UpdateView.as_view(
             template_name='registro/user_form.html',
             success_url=reverse_lazy('sec-home'),
             model=User,
             fields=[
                 'first_name',
                 'last_name',
                 'email',
             ],
         ), name='sec-completaDadosUsuario'),
]
