from django.contrib import admin

from .models import Event, DataRecording, DailyActivity, StartEvent, StartShedule


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


class StartAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('description', 'summary', 'location', 'day_delta', 'event_type')


class StartSheduleAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('description', 'run_interval', 'survey')


admin.site.register(Event, EventAdmin)
admin.site.register(DataRecording, DataRecordingAdmin)
admin.site.register(DailyActivity, DailyActivityAdmin)
admin.site.register(StartEvent, StartAdmin)
admin.site.register(StartShedule, StartSheduleAdmin)
