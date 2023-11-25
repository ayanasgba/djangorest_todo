from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

@api_view(['GET'])
def get_tasks_list(request):
    tasks = Task.objects.all()
    data = TaskSerializer(tasks, many=True).data
    return Response(data)

@api_view(['GET'])
def get_task_details(request, task_id):
    try:
        tasks = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = TaskSerializer(tasks)
    return Response(data.data)

@api_view(['POST'])
def create_task(request):
    data = TaskSerializer(data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)

    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_task(request, task_id):
    tasks = Task.objects.all(id=task_id)
    data = TaskSerializer(tasks, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_task(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    tasks.delete()
    return Response(status=status.HTTP_202_ACCEPTED)