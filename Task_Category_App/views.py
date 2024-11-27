from django.shortcuts import render,redirect
from .forms import CategoriesForm

# Create your views here.
def addCategory(request):
    if request.method == 'POST':
        categories_form = CategoriesForm(request.POST)
        if categories_form.is_valid():
            categories_form.save()
            return redirect('show_task_page')
    else:
        categories_form = CategoriesForm(request.POST)
    return render(request, 'Task_Category_App/add_category.html', {'categories_form' : categories_form})
