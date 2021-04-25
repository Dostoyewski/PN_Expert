from django.contrib import admin

from .models import SurveyShedule


class SurveySheduleAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('run_interval', 'survey')


admin.site.register(SurveyShedule, SurveySheduleAdmin)
