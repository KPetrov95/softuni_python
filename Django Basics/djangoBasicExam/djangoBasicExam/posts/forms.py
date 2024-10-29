from django import forms

from djangoBasicExam.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:'
        }
        widgets = {
            'title': forms.TextInput(),
            'image_url': forms.TextInput(),
            'content': forms.Textarea()
        }


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        model = Post
        fields = ['title', 'image_url', 'content']
        help_texts = {
            'image_url': 'Share your funniest furry photo URL!',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Put an attractive and unique title...',
                }),
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Share some interesting facts about your adorable pets...',
                }
            )
        }


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'