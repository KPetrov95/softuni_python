from django.shortcuts import render

from forumDemo.post.models import Post


def dashboard(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request,'posts/dashboard.html',context=context)