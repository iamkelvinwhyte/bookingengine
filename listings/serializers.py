from rest_framework import serializers

from .models import BookingInfo, Reservation, Listing
from django.core.exceptions import ValidationError


# Serializers for  Reservation.
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'listing_type', 'title', 'country', 'city']

# Serializers for  Reservation.


class BookingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingInfo
        fields = ['id', 'price']

# Serializers for  Reservation.


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'check_in', 'check_out', 'days', 'reservation_status',
                  'reservation_confirmation', 'confirmation_date']


class SelfValidationSerializer(serializers.Serializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()
    max_price = serializers.IntegerField()
