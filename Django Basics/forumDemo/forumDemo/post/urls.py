from django.urls import path

from forumDemo.post.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dash')
]