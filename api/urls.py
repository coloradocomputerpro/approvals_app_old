from django.urls import path
from .views import ApproverListCreateView, ApproverDetailView, ApproverTypeListCreateView, ApproverTypeDetailView

urlpatterns = [
    path('approvers/', ApproverListCreateView.as_view(), name='approver-list-create'),
    path('approvers/<int:pk>/', ApproverDetailView.as_view(), name='approver-detail'),
    path('approver-types/', ApproverTypeListCreateView.as_view(), name='approver-type-list-create'),
    path('approver-types/<int:pk>/', ApproverTypeDetailView.as_view(), name='approver-type-detail'),
]
