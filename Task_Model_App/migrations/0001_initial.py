# Generated by Django 5.1.3 on 2024-11-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Task_Category_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_description', models.TextField()),
                ('completed', models.BooleanField()),
                ('task_assign_date', models.DateField(default=False)),
                ('categories', models.ManyToManyField(to='Task_Category_App.categories')),
            ],
        ),
    ]
