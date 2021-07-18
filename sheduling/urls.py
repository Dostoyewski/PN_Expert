from django.urls import path

from . import views

urlpatterns = [
    path('api/shedules/reload', views.reload_all_shedules, name='reload_all'),
]
