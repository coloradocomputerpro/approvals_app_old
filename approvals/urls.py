from django.urls import path

from . import views

app_name = "approvals"

from .views import (
    ManageUsersAndGroupsView,
    UserUpdateView,
    UserDeleteView,
    UserCreateView,
    )

urlpatterns = [
    path("", views.index, name="index"),
    path("manage-notices/", views.manage_notices, name="manage_notices"),
    path("manage-users-groups/", ManageUsersAndGroupsView.as_view(), name="manage_users_groups"),
    path("user/create/", UserCreateView.as_view(), name="user_create"),
    path("user/<int:pk>/edit/", UserUpdateView.as_view(), name="user_edit"),
    path("user/<int:pk>/delete/", UserUpdateView.as_view(), name="user_delete"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

from django.urls import path
from .views import (
    RequestCreateView,
    RequestListView,
    RequestDetailView,
    RequestUpdateView,
    RequestDeleteView,
)

urlpatterns += [
    path("<int:pk>/", RequestDetailView.as_view(), name="request_detail"),
    path('requests/', RequestListView.as_view(), name='request_list'),
    path("request/create/", RequestCreateView.as_view(), name="request_create"),
    path("request/<int:pk>/delete/", RequestDeleteView.as_view(), name="request_delete"),
    path("request/<int:pk>/update/", RequestUpdateView.as_view(), name="request_update"),
]

from approvals.views import ProgramListView, ProgramCreateView

urlpatterns += [
    path('programs/', ProgramListView.as_view(), name='program_list'),
    path('program/create/', ProgramCreateView.as_view(), name='program_create'),
    path("program/<int:pk>/", views.ProgramDetailView.as_view(), name="program_detail"),
]
