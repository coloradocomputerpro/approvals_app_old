from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def get_approver_data(request):
    approver_users = list(User.objects.filter(groups__name='Approvers').values('id', 'username'))
    approver_types = ['end_client', 'systems_integrator', 'gov_body', 'vendor_pm', 'vendor_dev', 'vendor_adm']
    approver_subtypes = {'end_client': ['subtype1', 'subtype2', 'subtype3'],
                         'systems_integrator': ['subtype1', 'subtype2', 'subtype3'],
                         'gov_body': ['subtype1', 'subtype2', 'subtype3'],
                         'vendor_pm': ['subtype1', 'subtype2', 'subtype3'],
                         'vendor_dev': ['subtype1', 'subtype2', 'subtype3'],
                         'vendor_adm': ['subtype1', 'subtype2', 'subtype3']}
    data = {'approver_users': approver_users, 'approver_types': approver_types, 'approver_subtypes': approver_subtypes}
    return JsonResponse(json.dumps(data), safe=False)

from django.contrib.auth.models import User
from django.core import serializers

def get_users(request):
    users = User.objects.all().values('id', 'username')
    return JsonResponse(list(users), safe=False)