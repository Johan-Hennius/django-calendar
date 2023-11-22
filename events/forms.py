from django import forms
from django.forms import ModelForm
from .models import Venue


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = (
            'name',
            'address',
            'post_code',
            'email_address',
            'web_address'
        )