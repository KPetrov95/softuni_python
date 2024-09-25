from django.shortcuts import render

from UrlsAndViews.department.models import Department


# Create your views here.
def show_department_by_id(request, department_id):
    department = Department.objects.get(id=department_id)
    context = {
        "department": department
    }
    return render(request, "departments/index.html", context)


def show_department_by_name(request, department_name):
    department = Department.objects.get(name__exact=department_name)
    context = {
        "department": department
    }
    return render(request, "departments/index.html", context)
