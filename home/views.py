from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants, add_message
from django.contrib import messages

import re

def home(request):
    return render(request, 'home.html')

def termos(request):
    return render(request, 'termos.html')

def validando_login(request):
    login = request.POST.get('login')

    # TODO: deixar este aviso bonitinho
    if not login or not re.match("^[a-zA-Z0-9_]+$", login):
        messages.add_message(request, constants.ERROR, 'Login inválido. Use apenas letras, números e underscores.')
        return render(request, 'home.html')
    
    if request.method == "GET":
        return render(request, 'home.html')
    if request.method == "POST":
        usuario = User.objects.filter(username=login)
        if usuario.exists():
            return render(request, 'logar.html', {'usuario': login})
        else:
            return render(request, 'termos.html', {'usuario': login})

def concordando(request):
    login = request.POST.get('usuario')
    if request.method == "GET":
        return render(request, 'termos.html')
    if request.method == "POST":
        de_acordo = request.POST.get('checkTermos')
        if de_acordo:
            return render(request, 'cadastrar.html', {'usuario': login})
        else:
            # TODO: deixar este aviso bonitinho
            messages.add_message(request, constants.ERROR, 'Sem checar os termos é impossivel prosseguir.')
            return render(request, 'termos.html', {'usuario': login})