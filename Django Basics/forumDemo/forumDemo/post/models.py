from django.db import models

from forumDemo.user.models import User


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        to=User,
        related_name='posts',
        on_delete=models.DO_NOTHING
    )
    title = models.CharField(
        max_length=50,
        unique=True
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )