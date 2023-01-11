from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# Available time for booking training

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

# Status of booking


status_of_class = [
    ("confirmed", "confirmed"),
    ("rejected", "rejected"),
    ("In progress", "In progress")
]

# Trainers to choose

class_trainers = []
trainers = User.objects.filter(is_staff=True)
for trainer in trainers:
    class_trainers.append(((str(trainer.username)), str(trainer.username)))

# Booking specific trainer for a class


class Booking_class(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    trainers = models.CharField(max_length=10,
                                choices=class_trainers,
                                default="Karol")
    requested_date = models.DateField(null=True)
    requested_time = models.CharField(max_length=10, choices=TIME_CHOICES,
                                      default="10:00")
    status = models.CharField(max_length=15, choices=status_of_class,
                              default="In progress")


def __str__(self):

    return str(self.pk)
