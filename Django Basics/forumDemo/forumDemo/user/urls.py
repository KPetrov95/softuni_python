from django.urls import path

from forumDemo.user.views import index

urlpatterns = [
    path('home/', index, name='home')
]