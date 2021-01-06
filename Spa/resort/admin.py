from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'booking_date', 'email', 'created')
    list_filter = ('created',)


class SystemAdmin(admin.ModelAdmin):
    list_display = ('customer', 'booking', 'date_created')
    list_filter = ('date_created', )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(System, SystemAdmin)

