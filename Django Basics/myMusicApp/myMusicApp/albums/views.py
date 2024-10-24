from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from myMusicApp.albums.forms import AlbumAddForm, AlbumEditForm
from myMusicApp.albums.models import Album
from myMusicApp.utils import get_profile


class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumAddForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)

class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'

class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home-page')
    pk_url_kwarg = 'id'


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumEditForm
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home-page')
    pk_url_kwarg = 'id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
