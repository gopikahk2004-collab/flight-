# models is used to create database tables
from django.db import models

# Import Django's built-in User model
from django.contrib.auth.models import User

class Flight(models.Model):

    # Options for flight status
    STATUS_CHOICES = [

        ('Scheduled', 'Scheduled'),

        ('Delayed', 'Delayed'),

        ('Cancelled', 'Cancelled'),

        ('Completed', 'Completed'),

    ]

    # Flight number
    flight_number = models.CharField(
        max_length=20,
        unique=True
    )

    # Name of airline
    airline = models.CharField(
        max_length=100
    )

    # Starting location
    source = models.CharField(
        max_length=100
    )

    # Destination location
    destination = models.CharField(
        max_length=100
    )

    # Date of departure
    departure_date = models.DateField()

    # Time of departure
    departure_time = models.TimeField()

    # Flight price
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Number of available seats
    seats = models.IntegerField()

    # Current flight status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Scheduled'
    )

    # Display flight number in admin page
    def __str__(self):

        return self.flight_number

class Passenger(models.Model):

    # Name of passenger
    name = models.CharField(
        max_length=100
    )

    # Email of passenger
    email = models.EmailField()

    # Phone number of passenger
    phone = models.CharField(
        max_length=15
    )

    # Connect passenger with Django User
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Display passenger name in admin page
    def __str__(self):

        return self.name



# ============================================================
# CREATE BOOKING TABLE
# ============================================================

class Booking(models.Model):

    # Connect booking with passenger
    passenger = models.ForeignKey(
        Passenger,
        on_delete=models.CASCADE
    )

    # Connect booking with flight
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE
    )

    # Number of seats booked
    number_of_seats = models.IntegerField(
        default=1
    )

    # Automatically stores booking date and time
    booking_date = models.DateTimeField(
        auto_now_add=True
    )

    # Options for booking status
    STATUS_CHOICES = [

        ('Confirmed', 'Confirmed'),

        ('Cancelled', 'Cancelled'),

    ]

    # Current booking status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Confirmed'
    )

    # Prevent duplicate booking
    class Meta:

        unique_together = (
            'passenger',
            'flight'
        )

    # Display booking information in admin page
    def __str__(self):

        return (
            self.passenger.name
            + " - "
            + self.flight.flight_number
        )

