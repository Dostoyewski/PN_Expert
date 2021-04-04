from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>', views.profile, name='profile_detail'),
    path('account/', views.account, name='account'),
    path('account/update/', views.update_params, name='api_update_params'),
    path('diary/posts/', views.get_diary_list, name='api_diary'),
    path('accounts/login/', views.main_redirect_view, name='main_redirect'),
    path('news/', views.news_list, name='news_list'),
    path('api/profile/get/', views.get_user_info, name='profile_info'),
    path("api/profile/avatar/", views.UserAvatarUpload.as_view(), name="rest_user_avatar_upload"),
    path('api/profile/update/', views.write_user_info, name='profile_info_write'),
]
