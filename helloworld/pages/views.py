from django.shortcuts import render

# Create your views here.

# pages/views.py
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import TaskForm
from .models import Task
from django.shortcuts import redirect

def homePageView(request):
    return HttpResponse('Hello world')

def addPage(request):

    items = Task.objects.all().values('name')

    context= {
        'task_list': items,
    }

    return render(request, 'AddPage.html', context=context)

def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(name=form.cleaned_data['task_name'])
            task.save()
    return redirect('/')
        
        