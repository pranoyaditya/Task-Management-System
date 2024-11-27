from django.urls import path
from .import views

urlpatterns = [
    path('', views.addTask , name='add_task'),
    path('delete/<int:id>/', views.deleteTask, name='delete_task'),
    path('edit/<int:id>/', views.editTask, name='edit_task'),
]