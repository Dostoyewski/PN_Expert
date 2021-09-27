from django.contrib import admin

from .models import UserProfile, NewsRecording, DiaryRecording, StepsCounter, HADS_Result, HADS_Alarm, \
    SmileStats, ReactionStatistics, MemoryStatistics, ShwabStats, PDQ39Stats, DailyActivityStats


class ShwabAdmin(admin.ModelAdmin):
    list_display = ('user', 'value', 'day')


class PDQ39Admin(admin.ModelAdmin):
    list_display = ('user', 'value', 'day')


class UserProfileAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('user', 'name', 'vorname', 'fathername',
                    'gender', 'age', 'status', 'exp', 'isFull', 'slug')
    list_filter = ('user', 'name', 'gender', 'status', 'doctor')
    search_fields = ['user', 'doctor__user__username', 'doctor__user', 'doctor_name', 'name']


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


class ReactionAdmin(admin.ModelAdmin):
    """
    register steps counter
    """
    list_display = ('user', 'time', 'move', 'day')


class DailyActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'sleep_time', 'no_hom_time', 'work_time', 'sport_time')


class MemoryAdmin(admin.ModelAdmin):
    """
    register steps counter
    """
    list_display = ('user', 'turn', 'pairs', 'day')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(NewsRecording, NewsAdmin)
admin.site.register(DiaryRecording, DiaryAdmin)
admin.site.register(StepsCounter, StepAdmin)
admin.site.register(HADS_Result, HADSAdmin)
admin.site.register(HADS_Alarm, AlarmAdmin)
admin.site.register(SmileStats, SmileAdmin)
admin.site.register(ShwabStats, ShwabAdmin)
admin.site.register(PDQ39Stats, PDQ39Admin)
admin.site.register(DailyActivityStats, DailyActivityAdmin)
admin.site.register(ReactionStatistics, ReactionAdmin)
admin.site.register(MemoryStatistics, MemoryAdmin)
