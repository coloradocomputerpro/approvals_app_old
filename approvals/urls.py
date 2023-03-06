from django.urls import path

from . import views

app_name = "approvals"

urlpatterns = [
    path("", views.index, name="index"),
    path("manage-notices/", views.manage_notices, name="manage_notices"),
    path("manage-users-groups/", views.manage_users_groups, name="manage_users_groups"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

from django.urls import path
from .views import (
    RequestCreateView,
    RequestListView,
    RequestDetailView,
    RequestUpdateView,
)

urlpatterns += [
    path("", RequestListView.as_view(), name="index"),
    path("request/create/", RequestCreateView.as_view(), name="request_create"),
    path("<int:pk>/", RequestDetailView.as_view(), name="request_detail"),
    path("<int:pk>/update/", RequestUpdateView.as_view(), name="request_update"),
]

from approvals.views import ProgramListView, ProgramCreateView

urlpatterns += [
    path('programs/', ProgramListView.as_view(), name='program_list'),
    path('program/create/', ProgramCreateView.as_view(), name='program_create'),
    path("program/<int:pk>/", views.ProgramDetailView.as_view(), name="program_detail"),
]
