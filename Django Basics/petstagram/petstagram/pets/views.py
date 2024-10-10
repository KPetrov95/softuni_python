from django.shortcuts import render, redirect

from petstagram.pets.forms import PetForm, PetEditForm, DeletePetForm
from petstagram.pets.models import Pet


# Create your views here.
def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    context = {
        'pet': pet,
    }
    return render(request, 'pets/pet-details-page.html', context=context)


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


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = DeletePetForm(instance=pet)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    context = {'form': form,}

    return render(request, 'pets/pet-delete-page.html', context)
