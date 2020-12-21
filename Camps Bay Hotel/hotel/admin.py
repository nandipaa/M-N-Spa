from django.contrib import admin
from .models import *


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('guest', 'check_in', 'check_out')


class ReservedRoomAdmin(admin.ModelAdmin):
    list_display = ('number_of_rooms', 'room_category', 'reservation')


class RoomCategoryAdmin(admin.ModelAdmin):
    list_display = ('room_category', 'max_capacity')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'room_number', 'room_category')
    list_filter = ('status',)


admin.site.site_header = 'Camps Bay Hotel'
admin.site.register(RoomCategory, RoomCategoryAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservedRoom, ReservedRoomAdmin)


