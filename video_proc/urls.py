from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>', views.video_recording, name='video_rec'),
    path('api/video/competition/list/', views.competition_list, name='compet_list'),
    path('api/video/recording/create/', views.create_recording, name='create_rec'),
    path('api/photo/competition/list/', views.photo_competition_list, name='pcompet_list'),
    path('api/photo/recording/create/', views.photo_create_recording, name='pcreate_rec'),
]
