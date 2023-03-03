from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('manage-notices/', views.manage_notices, name='manage_notices'),
    path('manage-users-groups/', views.manage_users_groups, name='manage_users_groups'),
    
]