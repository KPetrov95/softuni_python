from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.common.forms import AddCommentForm
from petstagram.pets.forms import PetForm, PetEditForm, DeletePetForm
from petstagram.pets.models import Pet

# Create your views here.
class AddPetView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all()
        context['comment_form'] = AddCommentForm()

# def pet_details(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     context = {
#         'pet': pet,
#     }
#     return render(request, 'pets/pet-details-page.html', context=context)

class PetEditView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    def get_success_url(self):
        return reverse_lazy('pet-details', kwargs={'username': self.kwargs['username'],
                                                   'pet_slug': self.kwargs['pet_slug']})

def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
        return redirect('pet-details', username, pet_slug)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-edit-page.html', context)

class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    form_class = DeletePetForm
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('profile-details', pk=1)

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs

def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = DeletePetForm(instance=pet)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    context = {'form': form,}

    return render(request, 'pets/pet-delete-page.html', context)
