from django.shortcuts import render, redirect

from posts.forms.comment_form import CommentForm
from posts.forms.photo_add_form import AddForm
from posts.forms.post_edit_form import EditForm
from posts.models import Post, Like, Comment


def feed(request):
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'posts/feed.html', context)


def post_likes(request, pk):
    post = Post.objects.get(pk=pk)
    like = Like()
    like.post = post
    like.save()
    return redirect('post comments', pk)


def post_comments(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'post': post,
            'form': CommentForm(),
        }

        return render(request, 'posts/comment-page.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(comment=form.cleaned_data['comment'])
            comment.post = post
            comment.save()
            return redirect('post comments', pk)

        context = {
            'post': post,
            'form': form,
        }

        return render(request, 'posts/comment-page.html', context)


def add_photo(request):
    post = Post()
    if request.method == 'GET':
        form = AddForm()

        context = {
            'form': form,
        }

        return render(request, 'posts/add-photo.html', context)

    else:
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed')

        context = {
            'form': form,
        }

        return render(request, 'posts/add-photo.html', context)


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditForm(instance=post)

        context = {
            'form': form,
            'post': post,
        }

        return render(request, 'posts/post-edit.html', context)

    else:
        form = EditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed')

        context = {
            'form': form,
            'post': post,
        }

        return render(request, 'posts/post-edit.html', context)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'post': post
        }

        return render(request, 'posts/post-delete.html', context)
    else:
        post.delete()
        return redirect('feed')
