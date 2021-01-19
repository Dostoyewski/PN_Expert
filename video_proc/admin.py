from django.contrib import admin

from .models import Competition, CompetitionRecording


class CompetitionAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('header', 'text', 'video_ref', 'exp')
    prepopulated_fields = {'slug': ('header',)}


class CompetitionRecordingAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('published', 'video', 'trajectory', 'competition', 'user')


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(CompetitionRecording, CompetitionRecordingAdmin)
