from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
from django.db import IntegrityError

import re

def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        login = request.POST.get('login')
        if not login or not re.match("^[a-zA-Z0-9_]+$", login):
            messages.add_message(
                request, constants.ERROR, 'Login inválido. Use apenas letras, números e underscores.'
            )
            return redirect('/')
        usuario = User.objects.filter(username=login)
        if usuario.exists():
            return render(request, 'logar.html', {'usuario': login})
        else:
            return render(request, 'termos.html', {'usuario': login})

def termos(request):
    if request.method == "GET":
        return redirect('/')
    elif request.method == "POST":
        login = request.POST.get('usuario')
        de_acordo = request.POST.get('checkTermos')
        if de_acordo:
            return render(request, 'cadastrar.html', {'usuario': login})
        else:
            messages.add_message(request, constants.ERROR, 'Sem checar os termos é impossivel prosseguir.')
            return render(request, 'termos.html', {'usuario': login})

def realizando_cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')
    if request.method == "POST":
        login = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not login or not re.match("^[a-zA-Z0-9_]+$", login):
            messages.add_message(request, constants.ERROR, 'Login inválido. Use apenas letras, números e underscores.')
            return render(request, 'cadastrar.html', {'usuario': login})
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas divergentes!')
            return render(request, 'cadastrar.html', {'usuario': login})
        if not senha or not re.match("^[a-zA-Z0-9_]+$", senha):
            messages.add_message(request, constants.ERROR, 'Senha inválida. Use apenas letras, números e underscores.')
            return render(request, 'cadastrar.html', {'usuario': login})
        try:
            update = User.objects.filter(username=request.user).first()
            if not update:
                User.objects.create_user(
                username=login,
                password=senha
                )
                messages.success(request, 'Usuario registrado com sucesso.')
            else:
                update.username = login
                update.set_password(senha)
                update.save()
                messages.success(request, 'Usuario atualizado com sucesso.')
                logout(request)
            return redirect('/')
        except IntegrityError:
            messages.add_message(request, constants.ERROR, 'Erro ao atualizar o usuário. O nome de usuário já existe.')
            return render(request, 'cadastrar.html', {'usuario': login})
        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Erro interno do Servidor: {}'.format(str(e)))
            return render(request, 'cadastrar.html', {'usuario': login})

def logar(request):
    if request.method == "GET":
        return redirect('/')
    if request.method == "POST":
        login = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = auth.authenticate(request, username=login, password=senha)
        if usuario:
            auth.login(request, usuario)
            messages.add_message(request, constants.SUCCESS, 'Bem Vindo!')
            return redirect('/feed')
        else:
            messages.add_message(request, constants.ERROR, 'Senha inválida!')
            return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')