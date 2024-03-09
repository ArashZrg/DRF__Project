from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.get_all_todos),
    path('todos/<int:pk>', views.get_todo_detail),
    path('cbv/', views.TodosListView.as_view()),
    path('cbv/<int:pk>', views.TodosDetailView.as_view()),
    path('mixins/', views.TodosListMixins.as_view()),
    path('mixins/<int:pk>', views.TodosDetailMixins.as_view()),

]
