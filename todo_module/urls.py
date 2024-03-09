from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.get_all_todos),
    path('todos/<int:pk>', views.get_todo_detail)
]
