from django import forms
from forumDemo.post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('created_at',)

class DeletePostForm(PostForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True

class EditPostForm(PostForm):
    pass