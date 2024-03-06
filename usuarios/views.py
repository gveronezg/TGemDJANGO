from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
# from perfil.models import Tutor

import re

def cadastrar(request):
    return render(request, 'cadastrar.html')

def entrar(request):
    return render(request, 'logar.html')

def realizando_cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')
    if request.method == "POST":
        login = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas divergentes!')
            return render(request, 'cadastrar.html', {'usuario': login})
        if not senha or not re.match("^[a-zA-Z0-9_]+$", senha):
            messages.add_message(request, constants.ERROR, 'Senha inválida. Use apenas letras, números e underscores.')
            return render(request, 'cadastrar.html', {'usuario': login})
        try:
            User.objects.create_user(
                username=login,
                password=senha
            )
            return render(request, 'home.html')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do Servidor!')
            return render(request, 'cadastrar.html', {'usuario': login})
        
def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    if request.method == "POST":
        login = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(request, username=login, password=senha)

        if usuario:
            primeiro_acesso = usuario.last_login
            if primeiro_acesso is None:
                auth.login(request, usuario)
                messages.success(request, 'Usuário registrado com sucesso!')
                return redirect('/perfil/tutor/', usuario=login)
            else:
                auth.login(request, usuario)
                return render(request, 'tutor.html', {'usuario': login})
        else:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos!')
            return render(request, 'logar.html', {'usuario': login})

def logout(request):
    auth.logout(request)
    return render(request, 'home.html')