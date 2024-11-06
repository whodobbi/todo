from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
