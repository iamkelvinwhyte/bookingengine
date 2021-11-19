# Generated by Django 3.2 on 2021-11-18 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateField()),
                ('departure_date', models.DateField()),
                ('reservation_status', models.BooleanField()),
                ('reservation_confirmation', models.BooleanField()),
                ('confirmation_date', models.DateTimeField(auto_now_add=True)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='admin_reservation', to=settings.AUTH_USER_MODEL)),
                ('booking_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='booking_r', to='listings.bookinginfo')),
            ],
        ),
    ]