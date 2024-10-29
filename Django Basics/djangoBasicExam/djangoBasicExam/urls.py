
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoBasicExam.common.urls')),
    path('author/', include('djangoBasicExam.authors.urls')),
    path('posts/', include('djangoBasicExam.posts.urls'))
]
