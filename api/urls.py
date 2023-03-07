from django.urls import path
from django.urls import path, include
from . import views

from .views import (
    ApproverListCreateView,
    ApproverDetailView,
    ApproverTypeListCreateView,
    ApproverTypeDetailView,
)

urlpatterns = [
    path("approvers/", ApproverListCreateView.as_view(), name="approver-list-create"),
    path("approvers/<int:pk>/", ApproverDetailView.as_view(), name="approver-detail"),
    path(
        "approver-types/",
        ApproverTypeListCreateView.as_view(),
        name="approver-type-list-create",
    ),
    path(
        "approver-types/<int:pk>/",
        ApproverTypeDetailView.as_view(),
        name="approver-type-detail",
    ),
]


# Users
urlpatterns += [
    path("users/", views.UserList.as_view(), name="user-list"),
]
