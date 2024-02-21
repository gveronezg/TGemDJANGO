from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants, add_message

def home(request):
    return render(request, 'home.html')

def entrar(request):
    if request.method == "GET":
        return redirect('home.html')
    if request.method == "POST":
        celular = request.POST.get('celular')

        # Verificar se o número de celular está presente no banco de dados
        user = User.objects.filter(id=celular)

        if user.exists():
            # Se o usuário existe, redirecione para a página de login com senha
            return redirect('/usuarios/logar/')

        else:
            # Se o usuário não existe, redirecione para a página de login com SMS
            # Aqui você pode adicionar a lógica para enviar o código SMS
            # e lidar com a autenticação via SMS
            # Exemplo:
            # - Gerar código SMS
            # - Enviar código SMS para o número de celular
            # - Armazenar temporariamente o código no servidor ou no banco de dados
            # - Redirecionar para a página de login com código SMS

            # Exemplo de como adicionar uma mensagem para informar que um código SMS foi enviado
            add_message(request, constants.SUCCESS, 'Código SMS enviado para o número de celular.')
            return redirect('/usuarios/login_sms/')  # Substitua pelo caminho real da página de login com código SMS

    # Se a requisição não for do tipo POST, renderize a página padrão
    return render(request, 'entrar.html')
