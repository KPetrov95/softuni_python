from django import forms

from worldOfSpeed.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }

class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['first_name', 'last_name', 'profile_picture']

class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'