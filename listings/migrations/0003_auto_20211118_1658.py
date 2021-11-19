# Generated by Django 3.2 on 2021-11-18 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_reservation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['confirmation_date']},
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='arrival_date',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='departure_date',
            new_name='check_out',
        ),
    ]