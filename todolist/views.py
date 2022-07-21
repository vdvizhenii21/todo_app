import imp
from django.shortcuts import render
from rest_framework import viewsets 
from .models import Task
from rest_framework.response import Response
from rest_framework import status 
from .permissions import IsAuthor, IsWorker, IsWorkerStatus
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer
    permission_classes = [IsAuthor|IsWorker] 
    permission_classes_by_action = { 
        'create': [IsAuthenticated], 
        'list': [IsAuthenticated], 
        'retrieve': [IsAuthor|IsWorker], 
        'partial_update': [IsAuthor|IsWorker&IsWorkerStatus], 
        'update': [IsAuthor], 
        'destroy': [IsAuthor], 
    } 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_permissions(self):
        return [permission() for permission in self.permission_classes_by_action[self.action]]
