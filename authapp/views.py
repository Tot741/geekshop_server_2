from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm
from authapp.models import User
from basket.models import Basket



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'GeekShop - Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.success(request, 'Вы успешно зарегистрировались! На вашу почту отправлено письмо для потверждения')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                messages.error('Ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Geekshop - Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Geekshop - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'authapp/profile.html', context)

def verify(request, id, hash):
    user = User.objects.get(id=id)
    if user.activation_key == hash and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = None
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'authapp/verification.html')
    else:
        print(f'error activation user: {user}')
        return render(request, 'authapp/verification.html')

def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.pk, user.activation_key])
    title = f'Подтверждение регистрации учетной записи {user.username}'
    message = f'Для подтверждения регистрации учетной записи {user.username} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.username], fail_silently=False)


@transaction.atomic
def edit(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        ext_profile_form = UserProfileEditForm(request.POST, instance=request.user.userprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        profile_form = UserProfileForm(instance=request.user)
        ext_profile_form = UserProfileEditForm(instance=request.user.userprofile)
    context = {
        'title': 'Редактрирование дополнительных данных',
        'profile_form': profile_form,
        'ext_profile_form': ext_profile_form
    }
    return render(request, 'authapp/edit.html', context)
