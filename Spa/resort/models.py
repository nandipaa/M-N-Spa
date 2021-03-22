from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    PACKAGES_CHOICES = [('FULL DAY SPA', 'Full Day Spa'),
                        ('HALF DAY SPA', 'Half Day Spa'),
                        ('MOONLIGHT SPA', 'Moonlight Spa')]
    packages = models.CharField(max_length=100,
                                choices=PACKAGES_CHOICES,
                                default='FULL DAY SPA', null=True)

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
                              default='ONE', null=True)

    booking_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    otp_code = models.CharField(max_length=6, null=True)

    def __str__(self):
        return f'{self.email}-{self.phone}-{self.people}-{self.packages}'


class Appointment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, null=True, on_delete=models.CASCADE, related_name='bookings')

    STATUS = [
               ('Pending', 'Pending'),
               ('Attended', 'Attended'),
               ('Missed', 'Missed'),
               ('Cancelled', 'Cancelled'), ]

    date_created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True,  default='Pending')






