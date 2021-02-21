from django.contrib import admin

from .models import Event, DataRecording


class EventAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('description', 'summary', 'location', 'start', 'end', 'user', 'event_type')


class DataRecordingAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('user', 'file')


admin.site.register(Event, EventAdmin)
admin.site.register(DataRecording, DataRecordingAdmin)
