# Add your Views Here
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime

from .models import Task

PENDING_TASKS = []
COMPLETED_TASKS = []

SERVER_START_TIME = datetime.datetime.now().strftime("%I:%M:%S %p %d-%b-%y")


def tasks_view(request):
    tasks = Task.objects.filter(deleted=False, completed=False)
    context = {"tasks": tasks, "time": SERVER_START_TIME}
    return render(request, "tasks.html", context)


def all_tasks_view(request):
    pend_tasks = Task.objects.filter(deleted=False, completed=False)
    compl_tasks = Task.objects.filter(deleted=False, completed=True)
    context = {"pending_tasks": pend_tasks, "completed_tasks": compl_tasks}
    return render(request, "all_tasks.html", context)


def add_task_view(request):
    new_task = request.GET.get("task")
    Task(title=new_task).save()
    # PENDING_TASKS.append(new_task)
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, task_id):
    Task.objects.filter(id=task_id).update(deleted=True)
    # PENDING_TASKS.pop(task_id-1)
    return HttpResponseRedirect("/tasks")


def delete_completed_task_view(request, task_id):
    Task.objects.filter(id=task_id).update(deleted=True)
    # COMPLETED_TASKS.pop(task_id-1)
    return HttpResponseRedirect("/completed_tasks")


def mark_complete_task_view(request, task_id):
    Task.objects.filter(id=task_id).update(completed=True)
    # task = PENDING_TASKS.pop(task_id-1)
    # COMPLETED_TASKS.append(task)
    return HttpResponseRedirect("/tasks")


def completed_tasks_view(request):
    tasks = Task.objects.all().filter(deleted=False, completed=True)
    context = {"tasks": tasks, "time": SERVER_START_TIME}
    return render(request, "completed_tasks.html", context)
