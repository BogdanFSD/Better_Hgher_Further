from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Select
from .models import Booking_class


class DateInput(forms.DateInput):
    input_type = 'date'


class Booking_class_form(forms.ModelForm):
    # requested_date = forms.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Booking_class
        fields = ('trainers', 'requested_date', 'requested_time')
        widgets = {
            'requested_date': DateInput(attrs={
                'class': "form-control text-center attr"
            }),
            'trainers': Select(attrs={
                'class': "form-control text-center attr"
            }),
            'requested_time': Select(attrs={
                'class': "form-control text-center attr"
            })
         }
