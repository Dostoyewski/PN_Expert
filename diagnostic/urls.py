from django.urls import path

from . import views

urlpatterns = [
    path('api/create_event/', views.create_event, name='create_event'),
    path('events/', views.get_all_events, name='event_list'),
    path('create_activity/', views.create_activity, name='create_activity'),
    path('api/event/current/', views.get_user_events, name='user_events'),
    path('api/doctor/event/current/', views.get_doctor_events, name='doctor_events'),
    path('api/file/upload/', views.FileView.as_view(), name='file_upload'),
    path('api/file/get/', views.get_user_files, name='file_get'),
    path('api/event/by_date/', views.get_event_by_date, name='file_get'),
    path('api/event/mark_as_done/', views.mark_as_done, name='done_event'),
    path('api/doctor/event/mark_as_done/', views.doctor_mark_as_done, name='done_event_doctor'),
    path('api/notification/get/', views.get_user_notifications, name='notifications'),
    path('api/notification/period/', views.get_push_period, name='period'),
    path('api/notification/mark_as_shown/', views.mark_notification_as_shown,
         name='note_shown'),
    path('api/media/upload/', views.MediaView.as_view(), name='media_upload'),
    path('api/media/get/', views.get_user_medias, name='media_get'),
]
