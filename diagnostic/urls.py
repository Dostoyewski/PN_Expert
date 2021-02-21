from django.urls import path

from . import views

urlpatterns = [
    path('create_event/', views.create_event, name='create_event'),
    path('events/', views.get_all_events, name='event_list'),
    path('load_file/', views.load_file, name='load_file'),
    path('file_list/', views.file_list, name='file_list'),
]
