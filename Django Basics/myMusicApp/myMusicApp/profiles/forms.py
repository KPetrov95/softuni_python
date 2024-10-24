from django import forms

from myMusicApp.mixins import PlaceholderMixin
from myMusicApp.profiles.models import Profile


class ProfileBaseForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileCreateForm(ProfileBaseForm):
    pass