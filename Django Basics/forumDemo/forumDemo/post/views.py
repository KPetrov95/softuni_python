from django.shortcuts import render, redirect

from forumDemo.post.forms import PostForm, DeletePostForm, EditPostForm, SearchBarForm
from forumDemo.post.models import Post


def dashboard(request):
    posts = Post.objects.all()
    search = SearchBarForm(request.GET)
    if request.method == 'GET':
        if search.is_valid():
            query = search.cleaned_data['query']
            posts = posts.filter(title__icontains=query)
    context = {
        'posts': posts,
        'search': search,
    }
    return render(request,'posts/dashboard.html',context=context)

def post_details(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/post-details.html', context=context)

def add_post(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)

def delete_post(request, id):
    post = Post.objects.get(id=id)
    form = DeletePostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    if request.method == 'POST':
        post.delete()
        return redirect('dash')
    return render(request, 'posts/post-delete.html', context=context)

def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)  # Bind the form to the POST data
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form = EditPostForm(instance=post)  # When GET request, render the form with the current instance

    context = {
        'form': form,
        'post': post
    }
    return render(request,'posts/post-edit.html', context=context)