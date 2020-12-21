from django.db import models
from django.contrib.auth.models import User


class Guest(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class RoomCategory(models.Model):
    beds = models.IntegerField(null=True)
    description = models.CharField(max_length=2000, null=True)
    max_capacity = models.IntegerField(null=True)
    ROOM_CATEGORIES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Hollywood Twin Room', 'Hollywood Twin Room'),
        ('Cabana', 'Cabana'),
        ('Studio', 'Studio'),
        ('Suite', 'Suite'),

    ]

    room_category = models.CharField(max_length=100, choices=ROOM_CATEGORIES, null=True)

    def __str__(self):
        return self.room_category


class Room(models.Model):
    room_name = models.CharField(max_length=100, null=True)
    room_number = models.FloatField(max_length=100)
    STATUS = [
        ('Available', 'Available'),
        ('Vacant', 'Vacant'),
        ('Occupied', 'Occupied'),
    ]

    status = models.CharField(max_length=100, choices=STATUS)
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.room_name


class Reservation(models.Model):
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    made_by = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.made_by


class ReservedRoom(models.Model):
    number_of_rooms = models.IntegerField()
    room_category = models.ForeignKey(RoomCategory,null=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return self.number_of_rooms


class OccupiedRoom(models.Model):
    check_in = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    check_out = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return self.room


class HostedAt(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    occupied_room = models.ForeignKey(OccupiedRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.guest


