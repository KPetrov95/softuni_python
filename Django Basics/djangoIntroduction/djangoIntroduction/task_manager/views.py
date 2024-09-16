from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from djangoIntroduction.task_manager.models import Task


def index(request):
    query_filter = request.GET.get('query_filter', '')
    query = Q(name__icontains=filter) | Q(priority__icontains=filter) | Q(description__icontains=filter)
    tasks = Task.objects.filter(query)
    context = {
        "tasks": tasks,
        "query_filter": query_filter
    }

    return render(request, 'task_manager/index.html', context=context)
