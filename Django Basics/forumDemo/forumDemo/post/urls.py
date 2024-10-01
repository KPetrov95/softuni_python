from django.urls import path, include

from forumDemo.post import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dash'),
    path('add-post/', views.add_post, name='add-post'),
    path('post/<int:id>/', include([
        path('',views.post_details, name='post'),
        path('delete-post/', views.delete_post, name='delete-post'),
        path('edit-post/', views.edit_post, name='edit-post')

]))]