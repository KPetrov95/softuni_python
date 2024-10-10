from django.shortcuts import render, redirect, resolve_url

from petstagram.common.forms import AddCommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo
from pyperclip import copy


# Create your views here.

def home_page(request):
    all_photos = Photo.objects.all()
    comment_form = AddCommentForm()
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        all_photos = Photo.objects.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])
    context = {
        'comment_form': comment_form,
        'all_photos': all_photos,
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context=context)


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
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details',photo_id ))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

def comment_functionality(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=photo_id)
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')