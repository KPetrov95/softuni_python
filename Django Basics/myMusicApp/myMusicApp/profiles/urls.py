from django.urls import path

from myMusicApp.profiles import views

urlpatterns = [
    path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]