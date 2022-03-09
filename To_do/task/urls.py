from django.urls import path, include
from task import views

urlpatterns = [
    path('', views.home),
    path('tasks/', views.list_task, name="list_task"),
    path('tasks/<int:task_id>/', views.task_view, name="task_view"),
    path('tasks/create', views.task_create, name="task_create"),
    path('tasks/update<str:pk>/', views.task_update, name="task_update"),
]
