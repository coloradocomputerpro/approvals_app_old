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
router.register(r'requests', views.RequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from .views import ProgramMemberAddView
# Users
urlpatterns += [
    path("users/", views.UserList.as_view(), name="user-list"),
    path('program_member_add/', ProgramMemberAddView.as_view(), name='program_member_add'),

]
