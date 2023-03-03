from django.db import models


class TodoTask(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200)
    created_at = models.DateField(null=False, auto_now_add=True)

    def __str__(self):
        return self.name
