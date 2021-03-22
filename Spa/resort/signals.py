from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import *
from django.dispatch import receiver

from django.contrib.auth.models import Group


def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
        )


post_save.connect(customer_profile, sender=User)


def save_booking(sender, instance, created, **kwargs):
    if created:
        Appointment.objects.get(
            user=instance.user,
            booking=instance,

        )

        instance.save()


post_save.connect(save_booking, sender=Booking, dispatch_uid="my_unique_identifier")
