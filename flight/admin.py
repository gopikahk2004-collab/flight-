from django.contrib import admin

# Import our models
from .models import Flight, Passenger, Booking


# Show Flight in Django admin
admin.site.register(Flight)

# Show Passenger in Django admin
admin.site.register(Passenger)

# Show Booking in Django admin
admin.site.register(Booking)