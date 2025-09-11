from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Todo

# Create your views here.


def todolist(request):
    todos = Todo.objects.all()
    return render(request, "todo/todolist.html", {"todos": todos})


def index(request):  # 9/5 2:35:00
    return HttpResponse("<h1>Hello Django !!!</h1>")


def books(request):
    my_books = {"1": "Python", "2": "Django", "3": "Java"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
