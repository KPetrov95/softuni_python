from django.urls import path

from UrlsAndViews.department.views import show_department_by_id, show_department_by_name

urlpatterns = [
    path('<int:department_id>/', show_department_by_id),
    path('<str:department_name>/', show_department_by_name),
]