from datetime import datetime

from django.forms import modelform_factory
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import classonlymethod
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, FormView, CreateView, UpdateView, DeleteView, \
    DetailView

from ForumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from ForumApp.posts.models import Post


class BaseView:
    @classonlymethod
    def as_view(cls):

        def view(request, *args, **kwargs):
            view_instance = cls()
            return view_instance.dispatch(request, *args, **kwargs)

        return view

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.get(request, *args, **kwargs)
        elif request.method == "POST":
            return self.post(request, *args, **kwargs)


class IndexView(TemplateView):
    template_name = 'common/index.html'  # static way
    extra_context = {
        'static_time': datetime.now(),
    }  # static way

    def get_context_data(self, **kwargs):  # dynamic way
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']
        else:
            return ['common/index.html']


class Index(View):
    def get(self, request, *args, **kwargs):
        context = {
            'dynamic_time': datetime.now()
        }

        return render(request, 'common/index.html', context)



# def index(request):
#     post_form = modelform_factory(
#         Post,
#         fields=('title', 'content', 'author', 'languages' ),
#     )
#
#     context = {
#         "my_form": post_form,
#     }
#
#     return render(request, 'common/index.html', context)


class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    form_class = SearchForm
    success_url = reverse_lazy('dash')
    model = Post

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = self.queryset.filter(title__icontains=query)

        return queryset


# def dashboard(request):
#     form = SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == "GET":
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)


class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dash')


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dash')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'languages'))
        else:
            return modelform_factory(Post, fields=('content',))


class PostDetailsView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()
            return redirect('details-post', pk=post.pk)

        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)

def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)
    formset = CommentFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

    context = {
        "post": post,
        "formset": formset,
    }

    return render(request, 'posts/details-post.html', context)


class DeletePostView(DeleteView, FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__

class RedirectHomeView(RedirectView):
    url = reverse_lazy('index')  # static way

    # def get_redirect_url(self, *args, **kwargs):  # dynamic_way
    #     pass
    #