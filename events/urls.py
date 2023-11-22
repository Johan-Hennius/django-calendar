from django.urls import path
from . import views

"""
    Path Converters:

    int: numbers
    str: strings
    path: whole URLS
    slug: hyphenated-and_underscored 
    UUID: Universally unique identifier

"""
urlpatterns = [
    path('', views.home, name="home"),
    path('add-venue/', views.add_venue, name='add-venue'),
    path('add-event/', views.add_event, name='add-event'),
    path('<int:year>/<str:month>/', views.home, name="specific-date"),
    path('events/', views.events_list, name="events-list"),
    path('venues/', views.venues_list, name="venues-list"),
    path('show-venue/<venue_id>', views.show_venue, name='show-venue'),
]
