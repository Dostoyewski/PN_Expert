from django.urls import path

from . import views

urlpatterns = [
    path('api/pills/assignee/', views.create_pill_assigment, name='pill_assigment'),
]
