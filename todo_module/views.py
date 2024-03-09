from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status


# Create your views here.

@api_view(['Get', 'Post'])
def get_all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        serializer = TodoSerializer(todos, many=Todo)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['Get', 'Put', 'Delete'])
def get_todo_detail(request: Request, pk: int):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
