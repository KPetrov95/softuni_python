from django.core.validators import MinLengthValidator
from django.db import models

from djangoBasicExam.authors.validators import LettersValidator, ExactLengthValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(4), LettersValidator()]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), LettersValidator()]
    )
    passcode = models.CharField(
        max_length=6,
        validators=[ExactLengthValidator()],
        help_text='Your passcode must be a combination of 6 digits'
    )
    pets_number = models.PositiveSmallIntegerField()
    info = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
