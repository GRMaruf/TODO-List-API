from rest_framework import generics
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
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


@extend_schema_view(

    list=extend_schema(
        summary="Get all tasks",
        description="Returns a list of all tasks",
        tags=["Tasks"]
    ),

    retrieve=extend_schema(
        summary="Get single task",
        description="Returns details of a specific task",
        tags=["Tasks"]
    ),

    create=extend_schema(
        summary="Create task",
        description="Create a new task",
        tags=["Tasks"]
    ),

    update=extend_schema(
        summary="Update task",
        description="Update all fields of a task",
        tags=["Tasks"]
    ),

    partial_update=extend_schema(
        summary="Partial update task",
        description="Update specific fields of a task",
        tags=["Tasks"]
    ),

    destroy=extend_schema(
        summary="Delete task",
        description="Delete a task",
        tags=["Tasks"]
    ),

)
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer