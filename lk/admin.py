from django.contrib import admin

from .models import UserProfile, NewsRecording, DiaryRecording, StepsCounter, HADS_Result, HADS_Alarm, \
    SmileStats


class UserProfileAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('user', 'name', 'vorname', 'fathername',
                    'gender', 'age', 'status', 'exp', 'isFull', 'slug')


class NewsAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('header', 'text', 'published', 'img')


class DiaryAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('user', 'published', 'stimulators', 'brake', 'tremor')


class StepAdmin(admin.ModelAdmin):
    """
    register steps counter
    """
    list_display = ('user', 'steps')


class HADSAdmin(admin.ModelAdmin):
    """
    register steps counter
    """
    list_display = ('user', 'depression', 'day')


class AlarmAdmin(admin.ModelAdmin):
    """
    register steps counter
    """
    list_display = ('user', 'alarm', 'day')


class SmileAdmin(admin.ModelAdmin):
    """
    register steps counter
    """
    list_display = ('user', 'value', 'day')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(NewsRecording, NewsAdmin)
admin.site.register(DiaryRecording, DiaryAdmin)
admin.site.register(StepsCounter, StepAdmin)
admin.site.register(HADS_Result, HADSAdmin)
admin.site.register(HADS_Alarm, AlarmAdmin)
admin.site.register(SmileStats, SmileAdmin)
