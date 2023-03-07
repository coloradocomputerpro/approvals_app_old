from rest_framework import generics
from approvals.models import Approver, ApproverType
from .serializers import ApproverSerializer, ApproverTypeSerializer

class ApproverListCreateView(generics.ListCreateAPIView):
    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer

class ApproverDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer

class ApproverTypeListCreateView(generics.ListCreateAPIView):
    queryset = ApproverType.objects.all()
    serializer_class = ApproverTypeSerializer

class ApproverTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApproverType.objects.all()
    serializer_class = ApproverTypeSerializer
