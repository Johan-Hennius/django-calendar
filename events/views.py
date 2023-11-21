from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


# Create your views here.
def home(request, year, month):

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