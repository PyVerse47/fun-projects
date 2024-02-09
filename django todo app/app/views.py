from django.shortcuts import render, redirect
#from django.views.decorators.http import require_http_methods

from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(request, "base.html", {"todo_list": todos})


def add(request):
    title = request.POST["title"]
    todo = ToDo(title=title)
    todo.save()
    return redirect("index")


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.delete()
    return redirect("index")