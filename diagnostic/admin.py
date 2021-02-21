from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('description', 'summary', 'location', 'start', 'end', 'user', 'event_type')


admin.site.register(Event, EventAdmin)
