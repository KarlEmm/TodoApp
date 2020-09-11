from django.shortcuts import render
from .models import Task

def index(request):
  tasks = list(Task.objects.values())
  context = {
    "tasks": tasks
  }
  return render(request, "todos/index.html", context)

def task(request, task_id):
  task = Task.objects.get(id=task_id)
  context = {
    "task": task
  }
  return render(request, "todos/task.html", context)