from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AuthUser, UserRegister, Myprofile, EditProfile, ContactForm
from .models import Profil, User
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER


class all_pages(LoginRequiredMixin, ListView):
    model = Profil
    template_name = 'pages.html'
    context_object_name = 'pages'
    paginate_by = 2

    def get_queryset(self):
        return Profil.objects.select_related('profil')


@login_required
def my_profile(request):
    my_p = Profil.objects.filter(profil=request.user)
    context = {'pages': my_p}
    return render(request, 'profil.html', context)


@login_required
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


@login_required
def add_page(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = Myprofile(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.profil = user
            new_form.save()
            return redirect('profil')
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


# email
@login_required
def send_mes(request, user_id):
    user = Profil.objects.get(id=user_id)
    user_send = User.objects.get(id=user.profil.id)
    sender = User.objects.get(id=request.user.id)
    mail = sender.email
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            mail_mes = f'Здравствуйте, {user_send.username} \nВам отправили письмо с сайта AleksZ8.\n ' \
                       f'Отправитель данного письма {sender.first_name} {sender.last_name} {mail}  \n {form.cleaned_data["body"]}'
            send_mail(form.cleaned_data['subject'], mail_mes, EMAIL_HOST_USER, [user_send.email])
            return redirect('pages')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


@login_required
def delprofile(request, profile_id):
    profile = Profil.objects.filter(profil=request.user).get(id=profile_id)
    profile.delete()
    return redirect('profil')