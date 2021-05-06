from django.contrib import admin

from .models import SurveyShedule, MessageSurvey


class SurveySheduleAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('run_interval', 'survey')


class MessageSheduleAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('run_interval', 'message', 'typo')


admin.site.register(SurveyShedule, SurveySheduleAdmin)
admin.site.register(MessageSurvey, MessageSheduleAdmin)
