from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_training, name='booking'),
    path('Booked', views.check_booked_classes,
         name='booked'),

]
