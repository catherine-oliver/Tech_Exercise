from django import forms

class TaskForm(forms.Form):
    task_name= forms.CharField(label="task name", max_length=100)
