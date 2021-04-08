from django.urls import path

from . import views

urlpatterns = [
    path('api/create_event/', views.create_event, name='create_event'),
    path('events/', views.get_all_events, name='event_list'),
    path('load_file/', views.load_file, name='load_file'),
    path('file_list/', views.file_list, name='file_list'),
    path('create_activity/', views.create_activity, name='create_activity'),
    path('api/event/current/', views.get_user_events, name='user_events'),
    path('api/file/upload/', views.FileView.as_view(), name='file_upload'),
    path('api/file/get/', views.get_user_files, name='file_get'),
    path('api/event/by_date/', views.get_event_by_date, name='file_get'),
    path('api/event/mark_as_done/', views.mark_as_done, name='done_event'),
]
