from django import forms
from django.forms import ModelForm
from .models import Venue, Event


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

        labels = {
            'name': '',
            'address': '',
            'post_code': '',
            'email_address': '',
            'web_address': ''
            ,
        }

        # add style to form
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'Venue Name:'}),
            'address': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'Venue Address:'}),
            'post_code': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'Venue Post Code'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control mb-3', 'placeholder': 'Venue Email Address'}),
            'web_address': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'Venue Website'}),
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'name',
            'event_date',
            'venue',
            'description'
        )

        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'description': ''
        }

        # add style to form
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'Event Name:'}),
            'event_date': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'Event date and time:'}),
            'venue': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'Event venue'}),
            'description': forms.Textarea(attrs={'class':'form-control mb-3', 'placeholder': 'Event Description'})
        }

