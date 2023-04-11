from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
    STATUS_CHOICE = (
        ("In progess", "In progess"),
        ("Completed", "Completed"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(verbose_name="Task name",
                            max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE,
                               default="In progess")
    started_on = models.DateField(auto_now_add=True)
    ended_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.task