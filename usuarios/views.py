from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

def cadastrar(request):
    return render(request, 'cadastrar.html')

def logar(request):
    return render(request, 'logar.html')

def realizando_cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')
    if request.method == "POST":
        login = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # TODO: deixar este aviso bonitinho
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas divergentes!')
            return render(request, 'cadastrar.html', {'usuario': login})
        '''
        usuario = User.objects.filter(username=login)
        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já cadastrado!')
            return redirect('cadastrar.html', {'usuario': login})
        '''
        try:
            User.objects.create_user(
                username=login,
                password=senha
            )
            return render(request, 'home.html')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do Servidor!')
            return render(request, 'cadastrar.html', {'usuario': login})