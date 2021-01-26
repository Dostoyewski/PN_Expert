from django.urls import path

from . import views

urlpatterns = [
    path('send_push', views.send_push, name='send_push'),
    path('', views.home, name='home'),
]
