from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from worldOfSpeed.cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from worldOfSpeed.cars.models import Car
from worldOfSpeed.utils import get_profile


# Create your views here.
class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    success_url = reverse_lazy('catalogue')
    template_name = 'car/car-create.html'

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)


class CarCatalogueView(ListView):
    model = Car
    template_name = 'car/catalogue.html'


class CarDetailsView(DetailView):
    model = Car
    template_name = 'car/car-details.html'
    pk_url_kwarg = 'id'

class CarEditView(UpdateView):
    model = Car
    template_name = 'car/car-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')
    form_class = CarEditForm

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/car-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')
    form_class = CarDeleteForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

