from django.db import models

# Create your models here.


class TaskStoreModel(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)

