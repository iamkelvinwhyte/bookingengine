from django.http import response
from rest_framework.test import APITestCase
from rest_framework import status


# Create your tests here.


class ReservationList(APITestCase):

    def setUp(self):

        self.max_price = 100
        self.check_in = '2021-11-18'
        self.check_out = '2021-11-29'

    def test_reservation(self):
        response = self.client.get(
            '/api/v1/units?max_price={}&check_in={}&check_out={}'.format(self.max_price, self.check_in, self.check_out))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
