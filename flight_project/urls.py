from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # Django admin page
    path(
        'admin/',
        admin.site.urls
    ),

    # Connect flight application URLs
    path(
        '',
        include('flight.urls')
    ),
]