
from datetime import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BookingInfo, Reservation
from .serializers import SelfValidationSerializer
import time


# Get  ReservationList
class ReservationList(APIView):

    def get(self, request):
        start_time = time.time()
        serializer_data = SelfValidationSerializer(
            data=request.query_params)
        if not serializer_data.is_valid():
            return Response(serializer_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        data = []

        get_reservation = Reservation.objects.filter(
            check_in__gte=request.query_params['check_in'],
            check_out__lte=request.query_params['check_out']
        )
        # exclude date range from Booking
        get_booking = BookingInfo.objects.exclude(
            booking_r__in=get_reservation.all()
        )
        # filter query using max_price and order by price
        get_booking = get_booking.filter(
            price__lte=request.query_params['max_price']).order_by('price')

        for get_listing in get_booking:
            if get_listing.listing:
                _get_list = get_listing.listing
            else:
                _get_list = get_listing.hotel_room_type.hotel

            get_data = {
                "listing_type": _get_list.listing_type,
                "title": _get_list.title,
                "country": _get_list.country,
                "city": _get_list.city,
                "price": get_listing.price
            }
            data.append(get_data)

        print("Time complexity--- %s seconds ---" % (time.time() - start_time))
        return Response({'items': data},  status=status.HTTP_200_OK)
