from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants, add_message

def home(request):
    return render(request, 'home.html')

def termos(request):
    return render(request, 'termos.html')

def validando_login(request):
    login = request.POST.get('login')
    if request.method == "GET":
        return render(request, 'home.html')
    if request.method == "POST":
        usuario = User.objects.filter(username=login)
        if usuario.exists():
            return render(request, 'logar.html')
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
            return render(request, 'termos.html')