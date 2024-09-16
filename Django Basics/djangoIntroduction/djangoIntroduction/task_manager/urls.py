from django.urls import path
from djangoIntroduction.task_manager.views import index

urlpatterns = [
    path('', index)
]