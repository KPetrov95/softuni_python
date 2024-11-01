from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'date_of_publication', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join(str(pet) for pet in obj.tagged_pets.all())