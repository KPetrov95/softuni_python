from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from myMusicApp.profiles.validators import CharsValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[CharsValidator(), MinLengthValidator(2)]
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True
    )