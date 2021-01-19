from django.contrib import admin

from .models import UserProfile, NewsRecording


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


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(NewsRecording, NewsAdmin)
