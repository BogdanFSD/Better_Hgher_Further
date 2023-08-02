from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Select
from .models import BookingClass
from django.conf import settings
import datetime
from .utils import get_trainers


class DateInput(forms.DateInput):
    input_type = 'date'


class Booking_class_form(forms.ModelForm):
    trainers = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trainers'].choices = get_trainers()

    trainers = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control text-center attr"}),
        choices=[]
    )
    
    class Meta:
        model = BookingClass
        fields = ('trainers', 'requested_date', 'requested_time')
        widgets = {
            'requested_date': DateInput(
                attrs={'class': "form-control text-center attr",
                       'min': datetime.date.today()+datetime.timedelta(days=2),
                       'max': datetime.date.today()+datetime.timedelta(days=30)
                       }),
            'requested_time': Select(attrs={
                'class': "form-control text-center attr"
            })
         }
