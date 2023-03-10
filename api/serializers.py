from rest_framework import serializers
from approvals.models import Approver, ApproverType, Program

class ApproverSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')
    program_name = serializers.ReadOnlyField(source='program.name')
    program_id = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all(), source='program')
    
    class Meta:
        model = Approver
        fields = ['id', 'username', 'email', 'type', 'program_name', 'program_id']

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



class ProgramSerializer(serializers.ModelSerializer):
    approvers = ApproverSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = '__all__'

from rest_framework import serializers
from approvals.models import Approver




from rest_framework import serializers
from approvals.models import Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
