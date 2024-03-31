from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
from django.db import IntegrityError
from django.contrib.auth import authenticate
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
        if "delete" in request.POST:
            usuario, senha = request.POST.get('usuario'), request.POST.get('senha')
            user = authenticate(username=usuario, password=senha)
            try:
                if user is not None:
                    user.delete()
                    messages.success(request, 'Conta excluída com sucesso!')
                    return redirect('/')
                else:
                    messages.error(request, 'Para excluir a conta, entre com o login e senhas atuais.')
                    return render(request, 'cadastrar.html', {'usuario': request.user})
            except Exception as e:
                messages.add_message(request, constants.ERROR, 'Erro interno do Servidor: {}'.format(str(e)))
                return render(request, 'cadastrar.html', {'usuario': request.user})
        elif "create/update" in request.POST:
            login, senha, confirmar_senha = request.POST.get('usuario'), request.POST.get('senha'), request.POST.get('confirmar_senha')
            error_message = None
            if not login or not re.match("^[a-zA-Z0-9_]+$", login):
                error_message = 'Login inválido. Use apenas letras, números e underscores.'
            elif not senha == confirmar_senha:
                error_message = 'Senhas divergentes.'
            elif not senha or not re.match("^[a-zA-Z0-9_]+$", senha):
                error_message = 'Senha inválida. Use apenas letras, números e underscores.'
            if error_message:
                messages.add_message(request, constants.ERROR, error_message)
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
        else:
            messages.add_message(request, constants.ERROR, 'Erro!')
            return redirect('/')

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