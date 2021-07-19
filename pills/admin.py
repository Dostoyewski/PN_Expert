from django.contrib import admin

from .models import Pill, AssignedPill, PillsReseter


class PillAdmin(admin.ModelAdmin):
    """
    Register Pill to admin profiles
    """
    list_display = ('title', 'info', 'typo')


class PillAssignedAdmin(admin.ModelAdmin):
    """
    Register Pill to admin profiles
    """
    list_display = ('pill', 'user', 'is_taken', 'extra', 'dosege', 'time_out', 'time')


class PillResetAdmin(admin.ModelAdmin):
    list_display = ('time', 'pk')


admin.site.register(PillsReseter, PillResetAdmin)
admin.site.register(Pill, PillAdmin)
admin.site.register(AssignedPill, PillAssignedAdmin)
