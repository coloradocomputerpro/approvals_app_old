from django.urls import path
from django.urls import path, include
from . import views

from .views import (
    ApproverListCreateView,
    ApproverDetailView,
    ApproverTypeListCreateView,
    ApproverTypeDetailView,
)

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'programs', views.ProgramViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'approvers', views.ApproverViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



# Users
urlpatterns += [
    path("users/", views.UserList.as_view(), name="user-list"),
]
