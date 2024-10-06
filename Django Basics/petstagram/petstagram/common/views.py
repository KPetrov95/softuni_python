from django.shortcuts import render, redirect, resolve_url

from petstagram.common.models import Like
from petstagram.photos.models import Photo
from pyperclip import copy


# Create your views here.

def home_page(request):
    all_photos = Photo.objects.all()
    context = {
        'all_photos': all_photos,
    }
    return render(request, 'common/home-page.html')


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    like = Like.objects.filter(to_photo_id=photo.id).first()
    if like:
        like.delete()
    else:
        like = Like(to_photo_id=photo.id)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_functionality(request, photo_id):
    copy(request.META['HTTP_POST'] + resolve_url('photo-details',photo_id ))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
