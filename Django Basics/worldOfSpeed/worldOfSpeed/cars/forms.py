from django import forms

from worldOfSpeed.cars.models import Car
from worldOfSpeed.utils import get_profile


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)
        widgets = {
            'image_url': forms.TextInput(attrs={'placeholder':'https://...'})
        }


class CarCreateForm(CarBaseForm):
    pass

class CarEditForm(CarBaseForm):
    pass

class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

