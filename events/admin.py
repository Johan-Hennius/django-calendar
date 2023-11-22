from django.contrib import admin
from .models import Venue, EventUser, Event

# Register your models here.
# admin.site.register(Venue)
admin.site.register(EventUser)
# admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'post_code')
    order = ('name', )
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'slug', 'venue'), 'description', 'event_date', 'manager')
    list_display = ('name', 'venue', 'event_date')
    list_filter = ('event_date', 'venue')
    prepopulated_fields = {'slug': ('name',)}
