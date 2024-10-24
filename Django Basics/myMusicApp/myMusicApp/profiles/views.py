from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from myMusicApp.profiles.models import Profile
from myMusicApp.utils import get_profile


class ProfileDetailsView(DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return get_profile()
