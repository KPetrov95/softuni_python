from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from petstagram.common.forms import AddCommentForm
from petstagram.photos.forms import PhotoCreationForm, PhotoEditForm
from petstagram.photos.models import Photo

class AddPhotoView(CreateView):
    model = Photo
    form_class = PhotoCreationForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home-page')

# def add_photo(request):
#     form = PhotoCreationForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return redirect('home-page')
#     context = {'form': form}
#     return render(request, 'photos/photo-add-page.html', context)

class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = AddCommentForm()

        return context

# def photo_details(request, pk: int):
#
#     photo = Photo.objects.get(pk=pk)
#     comments = photo.comment_set.all()
#     likes = photo.like_set.all()
#
#     context = {
#         'photo': photo,
#         'comments': comments,
#         'likes': likes,
#     }
#
#
#     return render(request, 'photos/photo-details-page.html', context)

class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'
    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})
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