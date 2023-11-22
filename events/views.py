from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue, User
from .forms import VenueForm, EventForm


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__icontains=searched)
        events = Event.objects.filter(name__icontains=searched)
        return render(
            request,
            'events/search_venues.html',
            {
                'searched': searched,
                'venues': venues,
                'events': events
            }
        )
    else:
        return render(
            request,
            'events/search_venues.html',
            {

            }
        )


def show_venue(request, venue_id):

    venue = Venue.objects.get(pk=venue_id)
    return render(
        request,
        'events/show_venue.html',
        {
            'venue': venue
        })


def venues_list(request):
    venue_list = Venue.objects.all()
    return render(
        request,
        'events/venue.html',
        {
            'venue_list': venue_list
        })


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


def add_venue(request):

    submitted = False

    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        'events/add_venue.html',
        {
            'form': form,
            'submitted': submitted
        }
    )


def add_event(request):

    submitted = False

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        'events/add_event.html',
        {
            'form': form,
            'submitted': submitted
        }
    )


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