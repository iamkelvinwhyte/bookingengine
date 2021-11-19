from django.db import models
from django.core.exceptions import ValidationError
import datetime


class Listing(models.Model):
    HOTEL = 'hotel'
    APARTMENT = 'apartment'
    LISTING_TYPE_CHOICES = (
        ('hotel', 'Hotel'),
        ('apartment', 'Apartment'),
    )

    listing_type = models.CharField(
        max_length=16,
        choices=LISTING_TYPE_CHOICES,
        default=APARTMENT
    )
    title = models.CharField(max_length=255,)
    country = models.CharField(max_length=255,)
    city = models.CharField(max_length=255,)

    def __str__(self):
        return self.title


class HotelRoomType(models.Model):
    hotel = models.ForeignKey(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_room_types'
    )
    title = models.CharField(max_length=255,)

    def __str__(self):
        return f'{self.hotel} - {self.title}'


class HotelRoom(models.Model):
    hotel_room_type = models.ForeignKey(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_rooms'
    )
    room_number = models.CharField(max_length=255,)

    def __str__(self):
        return self.room_number


class BookingInfo(models.Model):
    listing = models.OneToOneField(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info'
    )
    hotel_room_type = models.OneToOneField(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        if self.listing:
            obj = self.listing
        else:
            obj = self.hotel_room_type
        # return str(obj)

        return f'{obj} {self.price}'


class Reservation(models.Model):
    booking_info = models.OneToOneField(
        BookingInfo, null=False, related_name='booking_r', on_delete=models.CASCADE)
    check_in = models.DateField(blank=False, null=False)
    check_out = models.DateField(blank=False, null=False)
    reservation_status = models.BooleanField()
    confirmation_date = models.DateTimeField(auto_now_add=True)
    assigned_by = models.ForeignKey(
        'auth.User', null=False, related_name='admin_reservation', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['confirmation_date']

    def __str__(self):
        return str(self.booking_info)

    def clean(self):
        check_in = self.check_in
        check_out = self.check_out
        if check_out <= check_in:
            raise ValidationError(
                "Departure date should be greater than Arrival date.")

    def days(self):
        check_in = datetime.datetime.strptime(
            self.check_in, "%Y-%m-%d %H:%M")
        check_out = datetime.datetime.strptime(
            self.check_out, "%Y-%m-%d %H:%M")
        diff = abs((check_out-check_in).days)
        return diff
