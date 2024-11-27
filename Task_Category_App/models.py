from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.category_name}'