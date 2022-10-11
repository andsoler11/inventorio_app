import hashlib
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from pprint import pprint

def homepage(request):
    return render(request, 'homepage.html')

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        username = email.split('@')[0]
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            pprint('entro aca')
            login(request, user)
            return redirect('homepage')
        else:
            pprint('salio por aca')
            messages.error(request, 'Usuario o contraseña incorrectos')

    context = {'page': 'login'}
    return render(request, 'login_register.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya existe')
            return redirect('register')

        username = email.split('@')[0]
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Usuario registrado correctamente')
        return redirect('homepage')


    context = {'page': 'register'}
    return render(request, 'login_register.html', context)

def userLogout(request):
    logout(request)
    return redirect('homepage')