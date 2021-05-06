from django.contrib import admin

from .models import Pill, AssignedPill


class PillAdmin(admin.ModelAdmin):
    """
    Register Pill to admin profiles
    """
    list_display = ('title', 'info', 'dosege', 'time_out', 'time1', 'time2', 'time3',
                    'time4', 'time5', 'extra')


class PillAssignedAdmin(admin.ModelAdmin):
    """
    Register Pill to admin profiles
    """
    list_display = ('pill', 'user')


admin.site.register(Pill, PillAdmin)
admin.site.register(AssignedPill, PillAssignedAdmin)
