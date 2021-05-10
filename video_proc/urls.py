from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>', views.video_recording, name='video_rec'),
    path('api/competition/list/', views.competition_list, name='compet_list'),
    path('api/recording/create/', views.create_recording, name='create_rec'),
]
