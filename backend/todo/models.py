from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return self.title
