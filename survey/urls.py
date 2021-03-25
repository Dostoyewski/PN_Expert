from django.urls import path

from . import views

urlpatterns = [
    path('api/answer/create/', views.create_answer, name='answer_create'),
    path('api/question/create/', views.create_question, name='question_create'),
    path('api/survey/get/', views.get_survey, name='survey_get'),
    path('api/survey/create/', views.create_survey, name='survey_create'),
]