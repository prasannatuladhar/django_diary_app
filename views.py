from django.shortcuts import render,redirect
from  .models import TodoApp
from .forms import TodoAppForms


def index(request):
    if request.method == "POST":
        form = TodoAppForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
            
    else:
        tasklist = TodoApp.objects.all()
        return render(request,'todo_app/index.html',{'tasklist':tasklist})

    


def done_task(request,task_id):
    task = TodoApp.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('index')

def undone_task(request,task_id):
    task = TodoApp.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('index')

def delete(request,task_id):
    task = TodoApp.objects.get(pk=task_id)
    task.delete()
    return redirect('index')    

def edit(request,task_id):
    if request.method == "POST":
        task = TodoApp.objects.get(pk=task_id)
        form = TodoAppForms(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        task = TodoApp.objects.get(pk=task_id)
        return render(request,'todo_app/edit.html',{'task':task})        




    