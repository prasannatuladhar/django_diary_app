from django import forms
from .models import TodoApp

class TodoAppForms(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['task','done']