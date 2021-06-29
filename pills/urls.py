from django.urls import path

from . import views

urlpatterns = [
    path('api/pills/assignee/', views.create_pill_assigment, name='pill_assigment'),
    path('api/pills/list/', views.get_pills_list, name='pill_list'),
    path('api/pills/view/', views.view_assigned_pills, name='pill_assignee'),
    path('api/pills/assignee/create/', views.create_pill_assigment, name='assignee_create'),
    path('api/pills/assignee/update/', views.update_time_taken, name='assignee_update'),
    path('api/pills/assignee/reset/', views.reset_time_taken, name='assignee_reset'),
    path('api/pills/assignee/delete/', views.delete_pill_assigment, name='assignee_delete'),
    path('api/pills/assignee/mark/', views.mark_as_old_assigment, name='mark_as_taken'),
    path('api/pills/assignee/update_time_out', views.update_time_out, name='update_time_out'),
    path('api/pills/create/', views.create_pill, name='pill_create'),
]
