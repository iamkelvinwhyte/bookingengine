# Django & Django REST framework List Test project.

The test project won't be used in any real environment.

## Initial Project setup

    git clone https://github.com/xsaysoft/bookingengine.git
    python -m venv venv
    pip install -r requirements.txt
    python manage.py runserver

## Request example:

http://127.0.0.1:8000/api/v1/units?max_price=200&check_in=2021-11-18&check_out=2021-11-29

## Response example:

{
"items": [
{
"listing_type": "hotel",
"title": "Hotel Lux 3***",
"country": "UK",
"city": "London",
"price": 70.0
},
{
"listing_type": "hotel",
"title": "Hotel Lux 3***",
"country": "UK",
"city": "London",
"price": 90.0
},
{
"listing_type": "apartment",
"title": "Modern 2 Bed Apartment by Tower Bridge",
"country": "UK",
"city": "London",
"price": 120.0
}
]
}
