from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import TodoTask


# def index(request: HttpRequest) -> HttpResponse:
#     return render(request, 'todo/todo_list.html')


class TaskListView(ListView):
    model = TodoTask
    template_name = 'todo/todo_list.html'


class TaskCreateView(CreateView):
    model = TodoTask
    fields = "name", "description"
    success_url = reverse_lazy('todo:todo-list')


class TaskDeleteView(DeleteView):
    model = TodoTask
    success_url = reverse_lazy('todo:todo-list')


class TaskUpdateView(UpdateView):
    model = TodoTask
    fields = 'name', 'description'
    template_name = 'todo/todotask_edit.html'
    success_url = reverse_lazy('todo:todo-list')
