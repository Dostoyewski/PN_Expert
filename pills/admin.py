from django.contrib import admin

from .models import Pill, AssignedPill


class PillAdmin(admin.ModelAdmin):
    """
    Register Pill to admin profiles
    """
    list_display = ('title', 'info', 'dosege', 'time_out', 'time', 'extra', 'is_taken', 'typo')


class PillAssignedAdmin(admin.ModelAdmin):
    """
    Register Pill to admin profiles
    """
    list_display = ('pill', 'user')


admin.site.register(Pill, PillAdmin)
admin.site.register(AssignedPill, PillAssignedAdmin)
