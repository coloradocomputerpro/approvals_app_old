from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manage-notices/', views.manage_notices, name='manage_notices'),
    path('manage-users-groups/', views.manage_users_groups, name='manage_users_groups'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]