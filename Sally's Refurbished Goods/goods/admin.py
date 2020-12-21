from django.contrib import admin
from .models import Clothes


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'price')


admin.site.register(Clothes, ClothesAdmin)
