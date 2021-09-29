from django.contrib import admin

from .models import Answer, Question, Survey, SurveyAnswer


class AnswerAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('question', 'answer', 'user')


class QuestionAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('survey', 'question', 'typo', 'choices', 'extra_placeholder')
    list_filter = ('survey', 'typo')


class SurveyAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('points', 'num_q', 'title', 'description')


class SurveyAnswerAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('survey', 'user', 'file')
    list_filter = ('user', 'survey')


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(SurveyAnswer, SurveyAnswerAdmin)
