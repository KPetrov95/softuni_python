from django.shortcuts import render, redirect

from petstagram.photos.models import Photo


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')

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
    context = {
        'photo': photo,
    }
    return render(request, 'photos/photo-edit-page.html', context)

def photo_delete(request, pk: int):
    Photo.objects.get(pk=pk).delete()
    return redirect('home-page')