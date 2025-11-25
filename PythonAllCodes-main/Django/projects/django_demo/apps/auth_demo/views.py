from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('auth_profile')
    else:
        form = UserCreationForm()
    return render(request, 'auth_demo/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('auth_profile')
    else:
        form = AuthenticationForm(request)
    return render(request, 'auth_demo/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('auth_login')


@login_required
def profile_view(request):
    return render(request, 'auth_demo/profile.html')
