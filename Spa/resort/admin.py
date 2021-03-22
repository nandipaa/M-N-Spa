from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_date', 'email', 'created')
    list_filter = ('created',)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking', 'date_created')
    list_filter = ('date_created', )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Appointment, AppointmentAdmin)

