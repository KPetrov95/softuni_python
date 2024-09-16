from django.db import models


class Task(models.Model):
    class PriorityChoices(models.TextChoices):
        HIGH = 'High', 'High'
        MEDIUM = 'Medium', 'Medium'
        LOW = 'Low', 'Low'
        NO_PRIORITY = 'No Priority', 'No Priority'

    name = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    priority = models.CharField(
        max_length=50,
        choices=PriorityChoices.choices
    )
    added_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    is_completed = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name