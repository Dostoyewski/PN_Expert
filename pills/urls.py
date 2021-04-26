from django.urls import path

from . import views

urlpatterns = [
    path('api/pills/assignee/', views.create_pill_assigment, name='pill_assigment'),
    path('api/pills/list/', views.get_pills_list, name='pill_list'),
    path('api/pills/view/', views.view_assigned_pills, name='pill_assignee'),
]
