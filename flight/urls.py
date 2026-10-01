from django.urls import path

# Import views
from . import views


urlpatterns = [


    path(

        '',

        views.home,

        name='home'

    ),

    # Registration
    path(
        'register/',
        views.register_view,
        name='register'
    ),

    # Login
    path(
        'login/',
        views.login_view,
        name='login'
    ),

    # Logout
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    # Dashboard
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # Add flight
    path(
        'flights/add/',
        views.add_flight,
        name='add_flight'
    ),

    # Flight list and search
    path(
        'flights/',
        views.flight_list,
        name='flight_list'
    ),

    # Edit flight
    path(
        'flights/edit/<int:id>/',
        views.edit_flight,
        name='edit_flight'
    ),

    # Delete flight
    path(
        'flights/delete/<int:id>/',
        views.delete_flight,
        name='delete_flight'
    ),

    # Add passenger
    path(
        'passengers/add/',
        views.add_passenger,
        name='add_passenger'
    ),

    # Passenger list
    path(
        'passengers/',
        views.passenger_list,
        name='passenger_list'
    ),

    # Edit passenger
    path(
        'passengers/edit/<int:id>/',
        views.edit_passenger,
        name='edit_passenger'
    ),

    # Delete passenger
    path(
        'passengers/delete/<int:id>/',
        views.delete_passenger,
        name='delete_passenger'
    ),

    # Book flight
    path(
        'book/',
        views.book_flight,
        name='book_flight'
    ),

    # Booking list
    path(
        'bookings/',
        views.booking_list,
        name='booking_list'
    ),

    # Cancel booking
    path(
        'bookings/cancel/<int:id>/',
        views.cancel_booking,
        name='cancel_booking'
    ),
]