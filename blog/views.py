from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import AuthUser, UserRegister, Myprofile
from .models import Profil, User


def profile(request):
    topic = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = Myprofile(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.profil = topic
            new_form.save()
            return redirect('home')
    else:
        form = Myprofile()
    return render(request, 'newprofile.html', {'form': form})



#RLL
def home(request):
    return render (request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegister()
    return render(request, 'register.html', {'form': form})


def quit(request):
    logout(request)
    return redirect('auth')


def authentication(request):
    if request.method == "POST":
        form = AuthUser(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthUser()
    return render(request, 'auth.html', {'form': form})