from django.db import models
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """ Task Serializer """
    class Meta:
        model = Task
        fields = ['id','name','details']
    
    def create(self, validated_data):
        """ create method to created object with valid data """
        task=Task(**validated_data)
        task.save()
        return {"id": task.id}
    
    def update(self, instance, validated_data):
        """ update method to update object with valid data """
        task=instance
        for key, value in validated_data.items():
            setattr(task, key, value)
        task.save()
        return {"id": task.id}