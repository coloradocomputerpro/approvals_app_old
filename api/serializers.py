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
