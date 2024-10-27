from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldOfSpeed.cars.choices import CarTypeChoices
from worldOfSpeed.cars.validators import YearValidator
from worldOfSpeed.profiles.models import Profile


class Car(models.Model):
    type = models.CharField(max_length=10, choices=CarTypeChoices.choices)
    model = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(1),
    ])
    year = models.IntegerField(validators=[YearValidator()])
    image_url = models.URLField(unique=True,
                                error_messages={'unique':'This image URL is already in use! Provide a new one.'})
    price = models.FloatField(validators=[MinValueValidator(1.0)])
    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name='cars')