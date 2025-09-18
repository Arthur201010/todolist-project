from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Todo
from .forms import TodoForm
from datetime import datetime

# Create your views here.


def create_todo(request):
    message = ""
    form = TodoForm()
    # POST 網頁按button後submit
    if request.method == "POST":
        form = TodoForm(request.POST)
        form.save()
        message = "寫入資料庫成功"
        return redirect("todolist")
    return render(request, "todo/create-todo.html", {"message": message, "form": form})


def create_todo1(request):
    message = ""
    # POST 網頁按button後submit
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get("title")
        if title == "":
            print("標題欄位不能為空!")
            message = "標題欄位不能為空!"
        else:
            text = request.POST.get("text")
            important = request.POST.get("important")

            important = True if important == "on" else False
            todo = Todo.objects.create(title=title, text=text, important=important)
            todo.save()
            message = "寫入資料庫成功"

    return render(request, "todo/create-todo1.html", {"message": message})


def delete_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
    except Exception as e:
        print(e)
    return redirect("todolist")


def view_todo(request, id):
    message = ""
    # 檢視目前
    try:
        todo = Todo.objects.get(id=id)
        form = TodoForm(instance=todo)
    except Exception as e:
        print(e)
    # 更新資料
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        todo = form.save(commit=False)
        if todo.completed:
            todo.date_completed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            todo.date_completed = None

        todo.save()
        message = "更新成功!!!"
        return redirect("todolist")
    return render(request, "todo/view-todo.html", {"form": form, "message": message})


# 1.新增todo.html
# 2.將todo 傳輸到{{todo}}
def view_todo1(request, id):
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
    # order_by 使用 - 號降序
    todos = Todo.objects.all().order_by("-created")
    return render(request, "todo/todolist.html", {"todos": todos})


def index(request):  # 9/5 2:35:00
    return HttpResponse("<h1>Hello Django !!!</h1>")


def books(request):
    my_books = {"1": "Python", "2": "Django", "3": "Java"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
