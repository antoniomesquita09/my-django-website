from django.contrib import admin
from django.urls import include, path
from MeuApp import views

app_name = 'MeuApp'  # Define the app_name here


urlpatterns = [
    path('', views.home, name='home'),
    path('join_ride/<int:ride_id>/', views.join_ride, name='join_ride'),
    path('add_ride/', views.add_ride, name='add_ride'),  # Define URL pattern for add_ride
    # path('join_ride/', views.join_ride, name='join_ride'), # Ensure this exists
    path('ride_list/', views.ride_list, name='ride_list'),
    # path('admin/', admin.site.urls),

    # New routes
    path('lista/', views.RideCreateView.as_view(), name='lista-caronas'),
    path('criar/', views.RideCreateView.as_view(), name='cria-carona'),
    path('editar/<int:ride_id>/', views.RideCreateView.as_view(), name='atualiza-carona'),
    path('apagar/', views.RideCreateView.as_view(), name='apaga-carona'),
]
