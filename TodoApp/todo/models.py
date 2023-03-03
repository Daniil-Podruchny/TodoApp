from django.db import models


class TodoTask(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200)
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField()

    def __str__(self):
        return self.name
