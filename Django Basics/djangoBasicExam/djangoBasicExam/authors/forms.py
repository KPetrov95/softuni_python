from django import forms

from djangoBasicExam.authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:',
            'info': 'Info:',
            'image_url': 'Profile Image URL:'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={}),
            'last_name': forms.TextInput(attrs={}),
            'passcode': forms.PasswordInput(attrs={}),
            'pets_number': forms.NumberInput(attrs={}),
            'info': forms.Textarea(attrs={}),
            'image_url': forms.URLInput(attrs={})
        }


class AuthorCreateForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name...',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name...',
            }),
            'passcode': forms.PasswordInput(attrs={
                'placeholder': 'Enter 6 digits...',
                'help_text': 'Your passcode must be a combination of 6 digits'
            }),
            'pets_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the number of your pets...',
            }),
        }


class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']
