from django.db import models
from django.contrib.auth.models import User


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
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    confirm_email = models.CharField(max_length=200, null=True)
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

    booking_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.name


class System(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    STATUS = [
        ('Pending', 'Pending'),
        ('Attended', 'Attended'),
        ('Missed', 'Missed'),
        ('Cancelled', 'Cancelled'),
    ]
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)



