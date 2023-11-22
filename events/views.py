from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue, User

def events_list(request):
    event_list = Event.objects.all()
    event_venue = Venue.objects.all()
    event_attendees = User.objects.all()
    return render(
        request,
        'events/events_list.html',
        {
            'event_list': event_list,
            'event_venue': event_venue,
            'event_attendees': event_attendees,
        })


# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):

    # change month to capitalize
    month = month.capitalize()

    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create basic calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # get current year
    now = datetime.now()
    current_year = now.year

    return render(
        request,
        'events/index.html',
        {
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal": cal,
            "current_year": current_year,         
        }
        )