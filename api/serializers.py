from rest_framework import serializers
from todo.models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'message',
        ]