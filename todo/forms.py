from django import forms
from .models import TodoList

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('task',)

class TodoListUpdateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('task','status')


