from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):

    name = models.CharField('Venue Name', max_length=120, unique=True)
    address = models.CharField('Venue Address', max_length=360)
    post_code = models.CharField('Venue Post Code', max_length=20)
    email_address = models.EmailField('Venue Email', blank=True)
    web_address = models.URLField('Venue Website', blank=True)


    def __str__(self):
        return self.name


class EventUser(models.Model):

    first_name = models.CharField('User First Name', max_length=60, unique=True)
    last_name = models.CharField('User Last Name', max_length=60, unique=True)
    email = models.EmailField('User Email')
    address = models.CharField('User Address', max_length=360, blank=True)
    post_code = models.CharField('User Post Code', max_length=20, blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Event(models.Model):

    name = models.CharField('Event Name', max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="event_location", blank=True)
    manager =  models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    attendees = models.ManyToManyField(EventUser, related_name="event_attendee", blank=True)


    def __str__(self):
        return self.name



