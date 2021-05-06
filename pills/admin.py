from django.contrib import admin

from .models import Pill, AssignedPill


class PillAdmin(admin.ModelAdmin):
    """
    Register Pill to admin profiles
    """
    list_display = ('title', 'info', 'time', 'typo')


class PillAssignedAdmin(admin.ModelAdmin):
    """
    Register Pill to admin profiles
    """
    list_display = ('pill', 'user', 'is_taken', 'extra', 'dosege', 'time_out')


admin.site.register(Pill, PillAdmin)
admin.site.register(AssignedPill, PillAssignedAdmin)
