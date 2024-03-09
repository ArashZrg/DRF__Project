from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodosViewSet, basename='todos')
urlpatterns = [
    path('todos/', views.get_all_todos),
    path('todos/<int:pk>', views.get_todo_detail),
    path('cbv/', views.TodosListView.as_view()),
    path('cbv/<int:pk>', views.TodosDetailView.as_view()),
    path('mixins/', views.TodosListMixins.as_view()),
    path('mixins/<int:pk>', views.TodosDetailMixins.as_view()),
    path('generics/', views.TodosListGenericApiView.as_view()),
    path('generics/<int:pk>', views.TodosDetailGenericApiView.as_view()),
    path('viewset/', include(router.urls))

]
