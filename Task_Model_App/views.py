from django.shortcuts import render,redirect
from .forms import taskModelForm
from .models import taskModel

# Create your views here.
def addTask(request):
    if request.method == 'POST':
        task_form = taskModelForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task_page')
    else:
        task_form = taskModelForm()
    return render(request, 'Task_Model_App/add_task.html', { 'task_form': task_form})

def editTask(request, id):
    task = taskModel.objects.get(pk=id)
    task_form = taskModelForm(instance = task)
    if request.method == 'POST':
        task_form = taskModelForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task_page')
    return render(request, 'Task_Model_App/add_task.html', {'task_form' : task_form})

def deleteTask(request, id):
    task = taskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_task_page')
