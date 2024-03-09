from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status, viewsets
from rest_framework import mixins, generics


# Create your views here.

# region Function Based Views
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


# endregion

# region Class Based Views

class TodosListView(APIView):

    def get(self, request: Request):
        todos = Todo.objects.order_by('priority').all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(None, status.HTTP_400_BAD_REQUEST)


class TodosDetailView(APIView):

    def get_object(self, pk: int):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int):
        todo = self.get_object(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        todo = self.get_object(pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        todo = self.get_object(pk=pk)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


# endregion

# region Mixins
class TodosListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.order_by('priority').all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class TodosDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.order_by('priority').all()

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# endregion

# region Generics
class TodosListGenericApiView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.order_by('priority').all()


class TodosDetailGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.order_by('priority').all()


# endregion

# region ViewSets
class TodosViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.order_by('priority').all()
# endregion
