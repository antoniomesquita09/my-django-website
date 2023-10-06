# My Django Ride-Sharing App User Guide

Welcome to the user guide for the Django Ride-Sharing App. This guide will provide a brief overview of the features and how to use them.

## Table of Contents

- [Registering and Logging In](#registering-and-logging-in)
- [Adding a Ride](#adding-a-ride)
- [Joining a Ride](#joining-a-ride)
- [Viewing Available Rides](#viewing-available-rides)
- [Logging Out](#logging-out)

## Registering and Logging In

**Registering:**
1. Navigate to the registration page.
2. Enter your desired username, email, and a secure password.
3. Click the `Register` button.

**Logging In:**
1. Navigate to the login page.
2. Enter your username and password.
3. Click the `Login` button.

## Adding a Ride

As a registered user, you can offer rides to other users.

1. Once logged in, navigate to the `Add a Ride` page.
2. Choose your desired `Departure Time` and input the `Destination`.
3. Click `Submit`. Your ride will be added to the list, and you will be listed as the driver.

## Joining a Ride

If you're looking for a ride, you can easily join one offered by another user.

1. Navigate to the `Ride List` page.
2. Browse the available rides.
3. If you find a suitable ride with available seats, click the `Join Ride` button.

## Viewing Available Rides

You can view all available rides and their details:

1. Navigate to the `Ride List` page.
2. Here, you'll see a list of all rides, including:
   - Driver's name
   - Departure time
   - Destination
   - Number of free seats
   - List of passengers

## Logging Out

When you're done, you can easily log out:

1. Click on the `Logout` button, usually located at the top-right corner.
2. You will be redirected to the home page, confirming that you have been logged out.

Check out your admin page on [http://localhost:8000/MeuApp](http://localhost:8000/MeuApp)

You can also create a superuser inside running with docker:

```bash
docker exec -it your_container_name /bin/bash
python manage.py createsuperuser
```
## To access the admin page and manage the SQLite DB, hit the server address with the endpoind /admin. For example, if you are running on localhost, 127.0.0.1:8000/admin
## Temporary Occasional Particularities with the code: 

1. When joining a ride, please avoid joining twice as the same user, as this limitation was not implemented yet. 
2. When creating a ride, avoid joining the same ride you created as driver, this is another limitation that was not implemented yet. 


