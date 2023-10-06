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


]
