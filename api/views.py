from rest_framework import generics
from rest_framework import viewsets
from todo.models import *
from .serializers import *

#
# Better version using DRF generics

# - 1. ListCreateAPIView
# - 2. RetrieveUpdateDestroyAPIView

# These reduce code massively.

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

#
# Most API endpoints are some combination of common CRUD 
# (Create-Read-Update-Delete) functionality. Here we can
# use - ModelViewSet

#

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer