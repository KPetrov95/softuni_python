from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from worldOfSpeed.profiles.forms import ProfileCreateForm, ProfileEditForm, EditProfileForm
from worldOfSpeed.profiles.models import Profile
from worldOfSpeed.utils import get_profile


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalogue')


class ProfileDetailsView(DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        total_price = profile.cars.aggregate(total_sum=Sum('price'))[
                          'total_sum'] or 0  # Sum of the 'price' field for related cars
        context['total_price'] = total_price
        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_profile()

class ProfileDeleteView(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return get_profile()