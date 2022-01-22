from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Task
from .serializers import TaskSerializer

class TaskView(APIView):
    """ API for task view """
    task_id_fetch = openapi.Parameter('task_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,description="If no task_id passed then all instances will be returned")
    task_id_del = openapi.Parameter('task_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,description="task_id is important field")


    # method to create a task
    @swagger_auto_schema(
        request_body=openapi.Schema(
        description="name field important",
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Important field & size below 100'),
            'details': openapi.Schema(type=openapi.TYPE_STRING, description='size below 500'),
        })
    )
    def post(self, request):
        """ API method to create a task """
        response = {}
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer_response = serializer.save()
                response['message'] = "Task is created"
                response['status'] = True
                response['data'] = {
                    'task_id': serializer_response["id"] ,
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                error = next(iter(serializer.errors))
                response["messagae"] = serializer.errors[str(error)][0]
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response['message'] = str(e)
            response['status'] = False
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


    # method to fetch task info 
    @swagger_auto_schema(manual_parameters=[task_id_fetch])
    def get(self, request):
        """ API method to fetch task info """
        response = {}
        try:
            queryset=Task.objects.all()
            task_id=request.GET.get('task_id',None)
            # in case task id is provided filter will be applied
            if task_id:
                queryset=queryset.filter(id=task_id)   
            serializer = TaskSerializer(queryset,many=True) 
            response['message'] = "Task fetched"
            response['status'] = True
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response['message'] = str(e)
            response['status'] = False
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # method to update a task 
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'task_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Important field'),
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Important field & size below 100'),
            'details': openapi.Schema(type=openapi.TYPE_STRING, description='size below 500'),
        }))
    def patch(self, request):
        """ API method to update a task """
        response = {}
        try:
            task_id=request.data.pop('task_id',None)
            if task_id is None:
                response['message'] = "Provide task_id"
                response['status'] = False
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            task = Task.objects.get(id=task_id) 
            if task is None:
                response['message'] = "Task object not found with provided task_id"
                response['status'] = False
                return Response(response, status=status.HTTP_404_NOT_FOUND)

            serializer = TaskSerializer(
                instance=task, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer_response=serializer.save()
                response['message'] = "Task updated successfully."
                response['status'] = True
                response['data'] = serializer_response['id']
                return Response(response, status=status.HTTP_200_OK)
            else:
                error = next(iter(serializer.errors))
                response["messagae"] = serializer.errors[str(error)][0]
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response['message'] = str(e)
            response['status'] = False
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


    # method to delete a task 
    @swagger_auto_schema(description="Important field",manual_parameters=[task_id_del])
    def delete(self, request):
        """ API method to delete task model instance """
        response = {}
        try:
            task_id=request.GET.get('task_id',None)
            if task_id is None:
                response['message'] = "Provide task_id"
                response['status'] = False
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            task = Task.objects.get(id=task_id)
            task.delete()
            response['message'] = "Task with given task id deleted"
            response['status'] = True
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response['message'] = str(e)
            response['status'] = False
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

