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


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404



class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
from rest_framework import generics, mixins
from rest_framework.renderers import BrowsableAPIRenderer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def programs(self, request, pk=None):
        user = self.get_object()
        programs = user.program_set.all()
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)


from approvals.models import Approver
from .serializers import ApproverSerializer

class ApproverList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer
    renderer_classes = [BrowsableAPIRenderer]  # add BrowsableAPIRenderer to render the API in the browser
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ApproverDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer
    renderer_classes = [BrowsableAPIRenderer]  # add BrowsableAPIRenderer to render the API in the browser
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from approvals.models import Program
from .serializers import ProgramSerializer
from .permissions import IsProgramMemberOrReadOnly

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsProgramMemberOrReadOnly]

    @action(detail=True, methods=['get'])
    def approvers(self, request, pk=None):
        program = self.get_object()
        approvers = program.approvers.all()
        serializer = ApproverSerializer(approvers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_approvers(self, request, pk=None):
        program = self.get_object()
        approver_ids = request.data.get('approvers', [])
        approvers = Approver.objects.filter(pk__in=approver_ids)
        program.approvers.add(*approvers)
        serializer = ProgramSerializer(program)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def remove_approvers(self, request, pk=None):
        program = self.get_object()
        approver_ids = request.data.get('approvers', [])
        approvers = Approver.objects.filter(pk__in=approver_ids)
        program.approvers.remove(*approvers)
        serializer = ProgramSerializer(program)
        return Response(serializer.data)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from approvals.models import Approver
from api.serializers import ApproverSerializer


from rest_framework import viewsets, permissions
from rest_framework.response import Response

from approvals.models import Approver
from .serializers import ApproverSerializer

class ApproverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows approvers to be viewed or edited.
    """
    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        program_id = serializer.validated_data['program']
        program = get_object_or_404(Program, pk=program_id)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        approver = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(approver, data=request.data)
        serializer.is_valid(raise_exception=True)
        program_id = serializer.validated_data['program']
        program = get_object_or_404(Program, pk=program_id)
        serializer.save()
        return Response(serializer.data)


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from approvals.models import Request
from .serializers import RequestSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    #permission_classes = [IsAuthenticated]
