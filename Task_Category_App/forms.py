from django import forms 
from .models import Categories

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
        widgets = {
            'category_name': forms.TextInput(attrs={
                'placeholder': 'Enter task title.'
            }),
        }