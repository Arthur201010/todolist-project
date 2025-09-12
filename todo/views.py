from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Todo

# Create your views here.


# 1.新增todo.html
# 2.將todo 傳輸到{{todo}}
def view_todo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)
    # context = {"id": todo.id, "title": todo.title}
    # return HttpResponse(
    #     json.dumps(context, ensure_ascii=False), content_type="application/json"
    # )   9/10 2:10:00
    return render(request, "todo/view-todo.html", {"todo": todo})


# 9/10 1:30:00
def todolist(request):
    todos = Todo.objects.all()
    return render(request, "todo/todolist.html", {"todos": todos})


def index(request):  # 9/5 2:35:00
    return HttpResponse("<h1>Hello Django !!!</h1>")


def books(request):
    my_books = {"1": "Python", "2": "Django", "3": "Java"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
