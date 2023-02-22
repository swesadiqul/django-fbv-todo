from django.db import models
from django.contrib.auth.models import User

class Priority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    short_description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
