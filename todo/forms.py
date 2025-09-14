from django.forms import ModelForm
from .models import Todo


# 9/12 1:30:00
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important", "completed"]
        # fields = "__all__"
