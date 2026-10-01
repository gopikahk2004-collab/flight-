from django import forms

# Import our models
from .models import Flight, Passenger, Booking

# Create form from Flight model
class FlightForm(forms.ModelForm):

    class Meta:

        # Form is connected to Flight model
        model = Flight

        # Fields displayed in form
        fields = [
            'flight_number',
            'airline',
            'source',
            'destination',
            'departure_date',
            'departure_time',
            'price',
            'seats',
            'status'
        ]



# ============================================================
# PASSENGER FORM
# ============================================================

# Create form from Passenger model
class PassengerForm(forms.ModelForm):

    class Meta:

        # Form is connected to Passenger model
        model = Passenger

        # Fields displayed in form
        fields = [
            'name',
            'email',
            'phone'
        ]



# ============================================================
# BOOKING FORM
# ============================================================

# Create form from Booking model
class BookingForm(forms.ModelForm):

    class Meta:

        # Form is connected to Booking model
        model = Booking

        # Fields displayed in form
        fields = [
            'passenger',
            'flight',
            'number_of_seats'
        ]