from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms.signup_form import SignupForm
from accounts.models import UserProfile


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'posts': user.userprofile.post_set.all(),
        }

        return render(request, 'accounts/profile.html', context)


def signup_profile(request):
    if request.method == 'GET':
        context = {
            'form': SignupForm(),
        }

        return render(request, 'accounts/signup.html', context)
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user
            )
            profile.save()
            login(request, user)
            return redirect('feed')

        context = {
            'form': form,
        }

        return render(request, 'accounts/signup.html', context)


def signout_user(request):
    logout(request)
    return redirect('index')
