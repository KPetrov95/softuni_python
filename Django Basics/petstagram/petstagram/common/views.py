from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView

from petstagram.common.forms import AddCommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo
from pyperclip import copy


# Create your views here.

class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = AddCommentForm()
        context['search_form'] = SearchForm(self.request.GET)

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')
        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name)
        return queryset


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