from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .utils import get_trainers

# Create your models here.

TIME_CHOICES = [
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00")
]

status_of_class = [
    ("confirmed", "confirmed"),
    ("rejected", "rejected"),
    ("In progress", "In progress")
]

# Booking specific trainer for a class


class BookingClass(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    trainers = models.CharField(max_length=20,
                                default="Karol")
    requested_date = models.DateField(null=True)
    requested_time = models.CharField(max_length=10, choices=TIME_CHOICES,
                                      default="10:00")
    status = models.CharField(max_length=15, choices=status_of_class,
                              default="In progress")


def __str__(self):

    return f"{self.user} - {self.trainers} - {self.status}"
