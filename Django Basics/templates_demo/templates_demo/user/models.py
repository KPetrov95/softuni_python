from datetime import date

from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(
        max_length=50,
        unique=True,
    )

    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50
    )

    birth_date = models.DateField()

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age
