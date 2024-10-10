from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreationForm, PhotoEditForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = PhotoCreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home-page')
    context = {'form': form}
    return render(request, 'photos/photo-add-page.html', context)

def photo_details(request, pk: int):

    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all()
    likes = photo.like_set.all()

    context = {
        'photo': photo,
        'comments': comments,
        'likes': likes,
    }


    return render(request, 'photos/photo-details-page.html', context)

def photo_edit(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)
    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'photos/photo-edit-page.html', context)

def photo_delete(request, pk: int):
    Photo.objects.get(pk=pk).delete()
    return redirect('home-page')