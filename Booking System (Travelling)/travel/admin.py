from django.contrib import admin
from .models import Booking, Contact


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'booking_date', 'created', 'status')
    list_filter = ('created', 'status')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created')
    list_filter = ('created',)


admin.site.site_title = 'M & N Spa Admin'
admin.site.site_header = 'M & N Spa'
admin.site.index_title = 'Dashboard'
admin.site.register(Booking, BookingAdmin)
admin.site.register(Contact, ContactAdmin)


admin.site.login_form = None
admin.site.index_template = 'admin/base_site.html'
app_index_template = None
login_template = None
logout_template = None
password_change_template = None
password_change_done_template = None
