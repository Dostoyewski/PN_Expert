from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('send_push/', views.send_push, name='send_push'),
    url(r'^webpush/', include('webpush.urls'))
]
