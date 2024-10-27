from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldOfSpeed.profiles.validators import CharsValidator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, message='Username must be at least 3 chars long!'),
            CharsValidator(message='Username must contain only letters, digits, and underscores!'),
    ])
    email = models.EmailField()
    age = models.IntegerField(
        validators=[MinValueValidator(21)],
        help_text='Age requirement: 21 years and above.'
    )
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)