from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Select
from .models import Booking_class
from django.conf import settings
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class Booking_class_form(forms.ModelForm):
    # requested_date = forms.DateField(input_formats=DATE_FORMAT)

    class Meta:
        model = Booking_class
        fields = ('trainers', 'requested_date', 'requested_time')
        widgets = {
            'requested_date': DateInput(
                attrs={'class': "form-control text-center attr",
                       'min': datetime.date.today()+datetime.timedelta(days=2),
                       'max': datetime.date.today()+datetime.timedelta(days=30)
                       }),
            'trainers': Select(attrs={
                'class': "form-control text-center attr"}),
            'requested_time': Select(attrs={
                'class': "form-control text-center attr"
            })
         }
