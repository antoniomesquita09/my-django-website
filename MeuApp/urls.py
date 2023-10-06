from django.urls import path
from MeuApp import views

app_name = 'MeuApp'  # Define the app_name here


urlpatterns = [
    # New routes
    path('lista/', views.RideCreateView.as_view(), name='lista-caronas'),
    path('criar/', views.RideCreateView.as_view(), name='cria-carona'),
    path('editar/<int:ride_id>/', views.RideCreateView.as_view(), name='atualiza-carona'),
    path('apagar/', views.RideCreateView.as_view(), name='apaga-carona'),
]
