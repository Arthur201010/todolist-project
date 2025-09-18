from django.forms import ModelForm
from .models import Todo


class CreateTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important"]


# 9/12 1:30:00
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important", "completed"]
        # fields = "__all__"
