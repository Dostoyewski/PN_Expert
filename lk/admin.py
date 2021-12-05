from django.contrib import admin

from lk.models import create_events
from sheduling.models import MessageSurvey, SurveyShedule
from .models import UserProfile, NewsRecording, DiaryRecording, StepsCounter, HADS_Result, HADS_Alarm, \
    SmileStats, ReactionStatistics, MemoryStatistics, ShwabStats, PDQ39Stats, DailyActivityStats


class ShwabAdmin(admin.ModelAdmin):
    list_display = ('user', 'value', 'day')


class PDQ39Admin(admin.ModelAdmin):
    list_display = ('user', 'value', 'day')


@admin.action(description='Сгенерировать заново расписание')
def reload_all(modeladmin, request, queryset):
    for obj in queryset:
        reload_all_events(obj)


def reload_all_events(user_profile):
    surveys = SurveyShedule.objects.filter(users=user_profile.user)
    m_surveys = MessageSurvey.objects.filter(users=user_profile.user)
    for surv in surveys:
        surv.delete()
    for m_surv in m_surveys:
        m_surv.delete()
    create_events(user_profile.user, user_profile)


class UserProfileAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('user', 'name', 'vorname', 'fathername',
                    'gender', 'age', 'status', 'exp', 'isFull', 'slug')
    list_filter = ('user', 'name', 'gender', 'status', 'doctor')
    search_fields = ['user', 'doctor__user__username', 'doctor__user', 'doctor_name', 'name']
    actions = [reload_all]


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
