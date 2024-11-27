from django.db import models
from Task_Category_App.models import Categories

# Create your models here.
class taskModel(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    task_assign_date = models.DateField(default=False)
    categories = models.ManyToManyField(Categories)
    completed = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.task_title}'