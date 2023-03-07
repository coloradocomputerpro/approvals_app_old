from django.urls import path
from .views import get_approver_data, get_users

urlpatterns = [
    # ... other URL patterns ...
    path('get_users/', get_users, name='get_users'),
    path('get_approver_data/', get_approver_data, name='get_approver_data'),
]