from django.db import models
from datetime import datetime, date


class Booking(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    number = models.IntegerField(null=True)
    email = models.EmailField(max_length=100)
    confirm_email = models.EmailField(max_length=100)
    PACKAGES_CHOICES = [('FULL DAY SPA', 'Full Day Spa'),
                        ('HALF DAY SPA', 'Half Day Spa'),
                        ('MOONLIGHT SPA', 'Moonlight Spa')]
    packages = models.CharField(max_length=100,
                                choices=PACKAGES_CHOICES,
                                default='FULL DAY SPA')

    PEOPLE_CHOICES = [('ONE', '1'),
                      ('TWO', '2'),
                      ('THREE', '3'),
                      ('FOUR', '4'),
                      ('FIVE', '5'),
                      ('SIX', '6'),
                      ('SEVEN', '7'),
                      ('EIGHT', '8'),
                      ('NINE', '9'),
                      ('TEN', '10'), ]
    people = models.CharField(max_length=100,
                              choices=PEOPLE_CHOICES,
                              default='ONE')

    booking_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    STATUS = [
        ('Pending', 'Pending'),
        ('Attended', 'Attended'),
        ('Missed', 'Missed'),
        ('Cancelled', 'Cancelled'),
    ]

    status = models.CharField(max_length=200, null=True, choices=STATUS)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)