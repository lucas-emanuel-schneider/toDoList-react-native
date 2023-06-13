from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    if not tasks:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_tasks = TaskSerializer(tasks, many=True)
    return Response(serialized_tasks.data, status=status.HTTP_200_OK)
