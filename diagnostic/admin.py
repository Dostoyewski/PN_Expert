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


class DailyActivityAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('user', 'steps', 'activity', 'standing', 'sitting', 'liing',
                    'upstairs', 'downstairs')


admin.site.register(Event, EventAdmin)
admin.site.register(DataRecording, DataRecordingAdmin)
