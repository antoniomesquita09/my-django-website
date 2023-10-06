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
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.CustomLogoutView.as_view(), name='logout'),

]
