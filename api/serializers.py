from rest_framework import serializers
from approvals.models import Approver, ApproverType

class ApproverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approver
        fields = '__all__'

class ApproverTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApproverType
        fields = '__all__'

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
