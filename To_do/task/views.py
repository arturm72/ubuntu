from django.shortcuts import render, HttpResponse, redirect
from task.forms import TaskForm, TaskModelForm
from task.models import Task
from .forms import TaskForm

# Create your views here.


def home(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            # Task.objects.create(name=name, description=description)
            Task.objects.create(**form.cleaned_data)
            return HttpResponse("Task is created")

    context = {"form": form}

    return render(request, "task/home.html", context)


# def home(request):
#
#     print("@@@@", request.user)
#     form = TaskModelForm()
#     if request.method == "POST":
#         form = TaskModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponse("Task is created")
#
#     context = {"form": form}
#
#     return render(request, "task/home.html", context)


def list_task(request):
    task_list = Task.objects.all()

    return render(request, "task/index.html", context={"tasks": task_list})


def task_view(request, task_id):
    task = Task.objects.get(id=task_id)

    return render(request, "task/task_view.html", {"task_object": task})


def task_create(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "task/new_task.html", context)


# def task_update(request):
#
#     context = {}
#     return render(request, "task/task_update.html", context)
