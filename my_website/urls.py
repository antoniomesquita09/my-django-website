from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from django.urls import include
from django.contrib import admin

from MeuSite import views
from MeuSite.views import MeuLoginView, MeuUpdateView

urlpatterns = [
    # Define the namespace here
    path('MeuApp/', include('MeuApp.urls', namespace='MeuApp')),
    path('admin/', admin.site.urls),
    path("contatos/", include('contatos.urls')),
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro/', views.registro, name='sec-registro'),
    path('accounts/login/', MeuLoginView.as_view(template_name='registro/login.html'), name='sec-login'),
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
         MeuUpdateView.as_view(
             template_name='registro/user_form.html',
             success_url=reverse_lazy('sec-home'),
             model=User,
             fields=[
                 'first_name',
                 'last_name',
                 'email',
             ],
         ), name='sec-completaDadosUsuario'),
    path('accounts/password_reset/', PasswordResetView.as_view(
        template_name='registro/password_reset_form.html',
        success_url=reverse_lazy('sec-password_reset_done'),
        html_email_template_name='registro/password_reset_email.html',
        subject_template_name='registro/password_reset_subject.txt',
        from_email='webmaster@meslin.com.br',
    ), name='password_reset'),
    path('accounts/password_reset_done/', PasswordResetDoneView.as_view(
        template_name='registro/password_reset_done.html',
    ), name='sec-password_reset_done'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='registro/password_reset_confirm.html',
             success_url=reverse_lazy('sec-password_reset_complete'),
         ), name='password_reset_confirm'),
    path('accounts/password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='registro/password_reset_complete.html'
    ), name='sec-password_reset_complete'),
]
