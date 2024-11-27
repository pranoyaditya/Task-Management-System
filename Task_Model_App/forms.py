from django import forms
from .models import taskModel

class taskModelForm(forms.ModelForm):
    class Meta:
        model = taskModel
        fields = '__all__'

        widgets = {
            'task_title': forms.TextInput(attrs={
                'placeholder': 'Enter task title.'
            }),
            'task_description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Enter task description.'
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'task_assign_date': forms.DateInput(attrs={
                'type': 'date',
            }),
            'categories': forms.SelectMultiple()
        }
