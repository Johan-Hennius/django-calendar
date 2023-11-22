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
    path('<int:year>/<str:month>/', views.home, name="specific-date"),
    path('events/', views.events_list, name="events-list"),
]
