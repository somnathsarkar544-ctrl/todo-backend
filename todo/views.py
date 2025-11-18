from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #only returns todos of logged-in user
        return Todo.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer): #auto-assign logged-in user
        serializer.save(user=self.request.user)
