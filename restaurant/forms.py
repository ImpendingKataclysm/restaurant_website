from django import forms

from .models import Reservation


class ReservationForm(forms.Form):
    location = forms.CharField()
    party_name = forms.CharField()
    party_size = forms.IntegerField()
    contact_phone = forms.CharField()
    date_reserved = forms.DateField()
    time_reserved = forms.TimeField()
