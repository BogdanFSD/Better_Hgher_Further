from django.urls import path

from . import views

urlpatterns = [
    path('', views.booking_training, name='booking'),
    path('booked_training', views.check_booked_classes,
         name='check_booked_classes'),

]
