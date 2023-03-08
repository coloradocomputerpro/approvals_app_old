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

from rest_framework import serializers
from approvals.models import Program, Approver

class ApproverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approver
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    approvers = ApproverSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = '__all__'

from rest_framework import serializers
from approvals.models import Approver


class ApproverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approver
        fields = ('id', 'user')
        read_only_fields = ('user',)

from rest_framework import serializers
from approvals.models import Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
