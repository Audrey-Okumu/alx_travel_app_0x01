#Create API ViewSets

from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    #ViewSet for managing Listings
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    #ViewSet for managing Bookings
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

"""
    Uses ModelViewSet → gives you full CRUD functionality automatically.

    Connects your models to serializers.

     DRF handles routes, validation, and responses for you.
"""