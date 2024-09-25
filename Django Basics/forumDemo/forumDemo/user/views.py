from django.shortcuts import render

from forumDemo.user.models import User


def index(request):
    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'base.html', context)