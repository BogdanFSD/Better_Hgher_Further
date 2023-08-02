from django.contrib import admin
from .models import BookingClass
# Register your models here.


@admin.register(BookingClass)
class Booking_class_Admin(admin.ModelAdmin):
    list_dsiplay = ('user', 'trainers',
                    'requested_date', 'requested_time', 'status')
