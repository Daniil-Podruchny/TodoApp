from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.TaskListView.as_view(), name="todo-list"),
    path('create-task/', views.TaskCreateView.as_view(), name="create-task"),
    path('<pk>:int/delete/', views.TaskDeleteView.as_view(), name="delete-task"),
    path('<pk>:int/update/', views.TaskUpdateView.as_view(), name="update-task"),
]