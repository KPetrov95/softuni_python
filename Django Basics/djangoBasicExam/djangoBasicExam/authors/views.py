from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from djangoBasicExam.authors.forms import AuthorCreateForm, AuthorEditForm
from djangoBasicExam.authors.models import Author
from djangoBasicExam.utils import get_author


# Create your views here.
class CreateAuthorView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('dashboard')

class AuthorDetailsView(DetailView):
    template_name = 'author/details-author.html'

    def get_object(self, queryset=None):
        return get_author()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        total_posts = author.posts.count() or 0
        last_edited_post = author.posts.order_by('-updated_at').first()
        context['author'] = author
        context['total_posts'] = total_posts
        context['last_edited_post'] = last_edited_post
        return context

class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'author/edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_object(self, queryset=None):
        return get_author()

class AuthorDeleteView(DeleteView):
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_author()