from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from functools import wraps
from django.http import HttpResponseRedirect
from .utils import ssl_redirect


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})


# @ssl_redirect
@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, pk=request.user.pk)
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(initial={
            'name': profile.name,
            'email': profile.email,
            'birthday': profile.birthday,
        })
    return render(request, 'accounts/edit_profile.html', {'form': form})