from django import forms
from django.forms import ModelForm
from .models import Booking_class


class DateInput(forms.DateInput):
    input_type = 'date'


class Booking_class_form(forms.ModelForm):
    # requested_date = forms.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Booking_class
        fields = ('trainers', 'requested_date', 'requested_time')
        widgets = {
            'requested_date': DateInput(),
        }
