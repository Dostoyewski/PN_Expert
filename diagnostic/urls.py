from django.urls import path

from . import views

urlpatterns = [
    path('create_event/', views.create_event, name='create_event'),
    path('events/', views.get_all_events, name='event_list'),
]
