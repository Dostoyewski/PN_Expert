from django.urls import path

from . import views

urlpatterns = [
    path('', views.competitions_list, name='competition_list'),
    path('<slug:slug>', views.video_recording, name='video_rec'),
    path('upload/', views.grishas_intro, name='intro'),
    path('upload_timer/', views.grishas_intro_timer, name='intro_timer')
]
