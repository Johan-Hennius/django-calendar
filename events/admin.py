from django.contrib import admin
from .models import Venue, User, Event

# Register your models here.
admin.site.register(Venue)
admin.site.register(User)
admin.site.register(Event)