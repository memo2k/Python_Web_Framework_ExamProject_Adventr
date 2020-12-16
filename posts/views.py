from django.shortcuts import render, redirect

from posts.models import Post, Like


def feed(request):
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'posts/feed.html', context)


def post_details(request, pk):
    context = {
        'post': Post.objects.get(pk=pk),
    }

    return render(request, 'posts/post_details.html', context)


def post_likes(request, pk):
    post = Post.objects.get(pk=pk)
    like = Like()
    like.post = post
    like.save()
    return redirect('post details', pk)
