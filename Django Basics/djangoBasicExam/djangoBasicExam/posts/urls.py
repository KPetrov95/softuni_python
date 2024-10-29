from django.urls import path, include

from djangoBasicExam.posts.views import CreatePostView, DetailsPostView, EditPostView, DeletePostView

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('<int:id>/', include([
        path('details/', DetailsPostView.as_view(), name='details-post'),
        path('edit/', EditPostView.as_view(), name='edit-post'),
        path('delete/', DeletePostView.as_view(), name='delete-post')
    ]))
]