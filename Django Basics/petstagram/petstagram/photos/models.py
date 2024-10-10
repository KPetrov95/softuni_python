from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import MaxSizeValidator


class Photo(models.Model):
    photo = models.ImageField(upload_to='images', validators=[MaxSizeValidator(5)])
    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10)],
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    tagged_pets = models.ManyToManyField(Pet,related_name='photos_tagged', blank=True)
    date_of_publication = models.DateField(auto_now_add=True)
    last_edited = models.DateField(auto_now=True)