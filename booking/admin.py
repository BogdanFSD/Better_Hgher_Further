from django.contrib import admin
from .models import Booking_class
# Register your models here.


@admin.register(Booking_class)
class Booking_class_Admin(admin.ModelAdmin):
    list_dsiplay = ('user', 'trainers',
        'requested_date', 'requested_time', 'status')