from django.urls import path

from . import views

urlpatterns = [
    path('api/answer/create/', views.create_answer, name='answer_create'),
    path('api/question/create/', views.create_question, name='question_create'),
    path('api/survey/get/', views.get_survey, name='survey_get'),
    path('api/survey/create/', views.create_survey, name='survey_create'),
    path('api/answer/get/', views.get_answer, name='get_answer'),
    path('api/survey/attend/', views.attendee_survey, name='attendee_survey'),
    path('api/survey/answer/', views.create_survey_answer, name='surv_answer_create'),
]
