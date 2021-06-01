from django.contrib import admin

from .models import UserProfile, NewsRecording, DiaryRecording, StepsCounter


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


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(NewsRecording, NewsAdmin)
admin.site.register(DiaryRecording, DiaryAdmin)
admin.site.register(StepsCounter, StepAdmin)
