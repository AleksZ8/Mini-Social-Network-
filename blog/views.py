from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView
from .forms import AuthUser, UserRegister, Myprofile, EditProfile, ContactForm
from .models import Profil, User
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER


class All_Pages(ListView):
    model = Profil
    template_name = 'pages.html'
    context_object_name = 'pages'
    paginate_by = 2

    def get_queryset(self):
        return Profil.objects.select_related('profil')


def my_profile(request):
    my_p = Profil.objects.filter(profil=request.user)
    context = {'pages': my_p}
    return render(request, 'profil.html', context)


def edit_profile(request, profile_id):
    profile = Profil.objects.filter(profil=request.user).get(id=profile_id)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.profil = user
            new_form.save()
            return redirect('home')
    else:
        form = EditProfile(instance=profile)
    return render(request, 'editprofile.html', {'form': form})


def add_page(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = Myprofile(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.profil = user
            new_form.save()
            return redirect('home')
    else:
        form = Myprofile()
    return render(request, 'newprofile.html', {'form': form})


# RLL
def home(request):
    return render(request, 'home.html')


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


#email
def send_mes(request, user_id):
    user = Profil.objects.get(id=user_id)
    user_send = User.objects.get(id=user.profil.id)
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['subject'], form.cleaned_data['body'], EMAIL_HOST_USER, [user_send.email])
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'user': user, 'us': user_send})