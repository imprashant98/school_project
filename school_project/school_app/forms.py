from django import forms
from .models import Event, Todo


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time']


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'completed']
