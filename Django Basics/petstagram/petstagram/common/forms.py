from django import forms

from petstagram.common.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets ={
            'text': forms.Textarea(attrs={'placeholder': 'Add Comment...'})
        }

class SearchForm(forms.Form):
    pet_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Search by Pet Name...'}
    ), required=False)