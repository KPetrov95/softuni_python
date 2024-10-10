from django import forms

from petstagram.photos.models import Photo

class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
class PhotoCreationForm(PhotoBaseForm):
    pass

class PhotoEditForm(PhotoCreationForm):
    class Meta(PhotoBaseForm.Meta):
        exclude = ('photo',)

class PhotoDeleteForm(PhotoBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True