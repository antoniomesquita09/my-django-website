from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MeuApp/', include('MeuApp.urls')),  # including app-level urls
]
