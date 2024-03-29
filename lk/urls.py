from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>', views.profile, name='profile_detail'),
    path('account/', views.account, name='account'),
    path('account/update/', views.update_params, name='api_update_params'),
    path('api/diary/get/', views.get_diary_list, name='api_diary'),
    path('api/diary/create/', views.create_diary_rec, name='create_diary'),
    path('accounts/login/', views.main_redirect_view, name='main_redirect'),
    path('news/', views.news_list, name='news_list'),
    path('api/profile/get/', views.get_user_info, name='profile_info'),
    path("api/profile/avatar/", views.UserAvatarUpload.as_view(), name="rest_user_avatar_upload"),
    path('api/profile/update/', views.write_user_info, name='profile_info_write'),
    path('api/profile/flags/', views.set_user_flags, name='set_user_flags'),
    path('api/steps/create/', views.create_steps, name='create_steps'),
    path('api/steps/get/', views.get_steps, name='get_steps'),
    path('api/user/id/', views.get_user_id, name='get_id_by_email'),
    path('api/hads/depression/', views.get_depression, name='get_depression'),
    path('api/hads/alarm/', views.get_alarm, name='get_alarm'),
    path('api/smiles/', views.get_smiles, name='get_smiles'),
    path('api/search/user/', views.search_user, name='search_user'),
    path('api/search/user/doctor/', views.search_user_doctor, name='search_doctor'),
    path('api/search/user/relative/', views.search_user_relative, name='search_rel'),
    path('api/profile/doctor/set/', views.connect_patient_to_arzt, name='set_doctor'),
    path('api/profile/doctor/get/', views.get_current_doctor, name='get_doctor'),
    path('api/profile/doctor/detach/', views.detach_arzt, name='detach_doctor'),
    path('api/game/memory/create/', views.create_mem_stats, name='create_mem'),
    path('api/game/reaction/create/', views.create_react_stats, name='create_react'),
    path('api/game/memory/get/', views.get_memory_stats, name='get_mem'),
    path('api/game/reaction/get/', views.get_reaction_stats, name='get_react'),
    path('api/schwabe/get/', views.get_schwabe, name='get_schwabe'),
    path('api/pdq/get/', views.get_PDQ_39, name='get_pdq'),
    path('api/UPDRS/get/', views.get_UPDRS_stats, name='get_updrs'),
    path('api/daily_activity/get/', views.get_daily_activity, name='get_daily'),
    path('api/profile/relative/set/', views.connect_patient_to_relative, name='set_rel'),
    path('api/profile/relative/get/', views.get_current_relative, name='get_rel'),
    path('api/profile/relative/detach/', views.detach_relative, name='detach_rel'),
]
