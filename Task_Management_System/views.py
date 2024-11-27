from django.shortcuts import render
from Task_Model_App.models import taskModel

def showTask(request):
    taskList = taskModel.objects.all()
    return render(request, 'show_task.html', {'taskList' : taskList})