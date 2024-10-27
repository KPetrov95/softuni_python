from django.urls import path

from worldOfSpeed.profiles.views import ProfileCreateView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create-profile'),
    path('details/', ProfileDetailsView.as_view(), name='profile-details'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete')

]