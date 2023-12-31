from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TaskSerializer, UserSerializer
from .models import Task
from django.http import JsonResponse
import json
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'X-CSRFToken': token})


@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Invalid request body'})

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'X-CSRFToken': get_token(request)})
            else:
                return JsonResponse({'error': 'Invalid username or password'})
        else:
            return JsonResponse({'error': 'Missing username or password'})


@api_view(['POST'])
def createUser(request):
    serialized_user = UserSerializer(data=request.data)
    if serialized_user.is_valid():
        serialized_user.save()
        token = get_token(request)
        return Response({'X-CSRFToken': token}, status=status.HTTP_201_CREATED)
    return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logoutUser(request):
    if request.method == 'POST':
        request.session.flush()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    if not tasks:
        return Response({'message': 'No tasks found'},
                        status=status.HTTP_404_NOT_FOUND)
    serialized_tasks = TaskSerializer(tasks, many=True)
    return Response(serialized_tasks.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serialized_task = TaskSerializer(task)
    return Response(serialized_task.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def taskCreate(request):
    serialized_task = TaskSerializer(data=request.data)
    if serialized_task.is_valid():
        serialized_task.save()
        return Response(serialized_task.data, status=status.HTTP_201_CREATED)
    return Response(serialized_task.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serialized_task = TaskSerializer(instance=task, data=request.data)
    if serialized_task.is_valid():
        serialized_task.save()
        return Response(serialized_task.data, status=status.HTTP_200_OK)
    return Response(serialized_task.errors, status=status.HTTP_400_BAD_REQUEST)
