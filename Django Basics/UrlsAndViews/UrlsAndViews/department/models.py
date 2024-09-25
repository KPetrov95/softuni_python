from django.db import models
from django.utils.text import slugify


# Create your models here.
class Department(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        unique=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )


    def __str__(self):
        return f'This is {self.name} department ({self.description if self.description else "No description"}) with id={self.id}'