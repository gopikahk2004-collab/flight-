from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

# Django built-in User
from django.contrib.auth.models import User

# Authentication functions
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

# Restrict pages to logged-in users
from django.contrib.auth.decorators import login_required

# Import models
from .models import Flight, Passenger, Booking

# Import forms
from .forms import (
    FlightForm,
    PassengerForm,
    BookingForm
)



# ============================================================
# HOME PAGE
# ============================================================

def home(request):

    # Display home.html
    return render(
        request,
        'home.html'
    )



# ============================================================
# REGISTER USER
# ============================================================

def register_view(request):

    # Check whether form was submitted
    if request.method == 'POST':

        # Get username from form
        username = request.POST['username']

        # Get password from form
        password = request.POST['password']

        # Create new Django user
        User.objects.create_user(
            username=username,
            password=password
        )

        # Go to login page
        return redirect('login')

    # Otherwise display registration page
    return render(
        request,
        'register.html'
    )



# ============================================================
# LOGIN USER
# ============================================================

def login_view(request):

    # Check if login form was submitted
    if request.method == 'POST':

        # Get username
        username = request.POST['username']

        # Get password
        password = request.POST['password']

        # Check username and password
        user = authenticate(
            request,
            username=username,
            password=password
        )

        # If user exists
        if user is not None:

            # Login the user
            login(
                request,
                user
            )

            # Go to dashboard
            return redirect('dashboard')

        else:

            # Display error
            return render(
                request,
                'login.html',
                {
                    'error':
                    'Invalid username or password'
                }
            )

    # Display login page
    return render(
        request,
        'login.html'
    )



# ============================================================
# LOGOUT USER
# ============================================================

def logout_view(request):

    # Logout current user
    logout(request)

    # Return to home
    return redirect('home')



# ============================================================
# DASHBOARD
# ============================================================

@login_required
def dashboard(request):

    # Count total flights
    flight_count = Flight.objects.count()

    # Count total passengers
    passenger_count = Passenger.objects.count()

    # Count total bookings
    booking_count = Booking.objects.count()

    # Display dashboard
    return render(
        request,
        'dashboard.html',
        {
            'flight_count': flight_count,
            'passenger_count': passenger_count,
            'booking_count': booking_count
        }
    )



# ============================================================
# CREATE / ADD FLIGHT
# ============================================================

@login_required
def add_flight(request):

    # If form is submitted
    if request.method == 'POST':

        # Get submitted form data
        form = FlightForm(
            request.POST
        )

        # Check form
        if form.is_valid():

            # Save flight to database
            form.save()

            # Go to flight list
            return redirect('flight_list')

    else:

        # Empty form
        form = FlightForm()

    # Display form
    return render(
        request,
        'add_flight.html',
        {
            'form': form
        }
    )



# ============================================================
# READ / DISPLAY FLIGHTS
# ============================================================

@login_required
def flight_list(request):

    # Get all flights
    flights = Flight.objects.all()

    # Get search values from URL
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    departure_date = request.GET.get(
        'departure_date'
    )

    # Search by source
    if source:

        flights = flights.filter(
            source__icontains=source
        )

    # Search by destination
    if destination:

        flights = flights.filter(
            destination__icontains=destination
        )

    # Search by departure date
    if departure_date:

        flights = flights.filter(
            departure_date=departure_date
        )

    # Display results
    return render(
        request,
        'flight_list.html',
        {
            'flights': flights
        }
    )



# ============================================================
# UPDATE / EDIT FLIGHT
# ============================================================

@login_required
def edit_flight(request, id):

    # Find flight
    flight = get_object_or_404(
        Flight,
        id=id
    )

    # If edit form submitted
    if request.method == 'POST':

        # Load submitted values
        form = FlightForm(
            request.POST,
            instance=flight
        )

        # Check form
        if form.is_valid():

            # Save changes
            form.save()

            # Return to flight list
            return redirect(
                'flight_list'
            )

    else:

        # Show existing data
        form = FlightForm(
            instance=flight
        )

    # Display edit page
    return render(
        request,
        'edit_flight.html',
        {
            'form': form
        }
    )



# ============================================================
# DELETE FLIGHT
# ============================================================

@login_required
def delete_flight(request, id):

    # Find flight
    flight = get_object_or_404(
        Flight,
        id=id
    )

    # Delete only when confirmation form submitted
    if request.method == 'POST':

        # Delete from database
        flight.delete()

        # Return to flight list
        return redirect(
            'flight_list'
        )

    # Show confirmation page
    return render(
        request,
        'delete_flight.html',
        {
            'flight': flight
        }
    )



# ============================================================
# CREATE / ADD PASSENGER
# ============================================================

@login_required
def add_passenger(request):

    # If form is submitted
    if request.method == 'POST':

        # Get submitted form data
        form = PassengerForm(
            request.POST
        )

        # Check form
        if form.is_valid():

            # Create object but don't save yet
            passenger = form.save(
                commit=False
            )

            # Connect passenger with logged-in user
            passenger.user = request.user

            # Save passenger
            passenger.save()

            # Go to passenger list
            return redirect(
                'passenger_list'
            )

    else:

        # Empty form
        form = PassengerForm()

    # Display form
    return render(
        request,
        'add_passenger.html',
        {
            'form': form
        }
    )



# ============================================================
# READ / DISPLAY PASSENGERS
# ============================================================

@login_required
def passenger_list(request):

    # Get all passengers
    passengers = Passenger.objects.all()

    # Display passenger list
    return render(
        request,
        'passenger_list.html',
        {
            'passengers': passengers
        }
    )



# ============================================================
# UPDATE / EDIT PASSENGER
# ============================================================

@login_required
def edit_passenger(request, id):

    # Find passenger
    passenger = get_object_or_404(
        Passenger,
        id=id
    )

    # If edit form submitted
    if request.method == 'POST':

        # Load submitted values
        form = PassengerForm(
            request.POST,
            instance=passenger
        )

        # Check form
        if form.is_valid():

            # Save changes
            form.save()

            # Return to passenger list
            return redirect(
                'passenger_list'
            )

    else:

        # Show existing data
        form = PassengerForm(
            instance=passenger
        )

    # Display edit page
    return render(
        request,
        'edit_passenger.html',
        {
            'form': form
        }
    )



# ============================================================
# DELETE PASSENGER
# ============================================================

@login_required
def delete_passenger(request, id):

    # Find passenger
    passenger = get_object_or_404(
        Passenger,
        id=id
    )

    # Delete only when confirmation submitted
    if request.method == 'POST':

        # Delete from database
        passenger.delete()

        # Return to passenger list
        return redirect(
            'passenger_list'
        )

    # Show confirmation page
    return render(
        request,
        'delete_passenger.html',
        {
            'passenger': passenger
        }
    )



# ============================================================
# CREATE / BOOK FLIGHT
# ============================================================

@login_required
def book_flight(request):

    # If booking form is submitted
    if request.method == 'POST':

        # Get submitted form data
        form = BookingForm(
            request.POST
        )

        # Check form
        if form.is_valid():

            # Get passenger
            passenger = form.cleaned_data[
                'passenger'
            ]

            # Get flight
            flight = form.cleaned_data[
                'flight'
            ]

            # Get number of seats
            number_of_seats = form.cleaned_data[
                'number_of_seats'
            ]

            # Check duplicate booking
            duplicate = Booking.objects.filter(
                passenger=passenger,
                flight=flight,
                status='Confirmed'
            ).exists()

            # If duplicate exists
            if duplicate:

                return render(
                    request,
                    'book_flight.html',
                    {
                        'form': form,
                        'error':
                        'Passenger has already booked this flight'
                    }
                )

            # Check available seats
            if number_of_seats > flight.seats:

                return render(
                    request,
                    'book_flight.html',
                    {
                        'form': form,
                        'error':
                        'Not enough seats available'
                    }
                )

            # Save booking
            booking = form.save()

            # Reduce available seats
            flight.seats = (
                flight.seats
                - number_of_seats
            )

            # Save flight changes
            flight.save()

            # Go to booking list
            return redirect(
                'booking_list'
            )

    else:

        # Empty booking form
        form = BookingForm()

    # Display booking page
    return render(
        request,
        'book_flight.html',
        {
            'form': form
        }
    )



# ============================================================
# READ / DISPLAY BOOKINGS
# ============================================================

@login_required
def booking_list(request):

    # Get bookings
    bookings = Booking.objects.all()

    # Display bookings
    return render(
        request,
        'booking_list.html',
        {
            'bookings': bookings
        }
    )



# ============================================================
# CANCEL BOOKING
# ============================================================

@login_required
def cancel_booking(request, id):

    # Find booking
    booking = get_object_or_404(
        Booking,
        id=id
    )

    # Cancel only when POST
    if request.method == 'POST':

        # Return seats to flight
        booking.flight.seats += (
            booking.number_of_seats
        )

        # Save flight
        booking.flight.save()

        # Change booking status
        booking.status = 'Cancelled'

        # Save booking
        booking.save()

        # Return to booking list
        return redirect(
            'booking_list'
        )

    # Display confirmation page
    return render(
        request,
        'cancel_booking.html',
        {
            'booking': booking
        }
    )