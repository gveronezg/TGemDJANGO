from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import auth
from django.contrib.messages import constants, add_message
from django.contrib import messages
from .models import Tutor

# import re

def tutor(request):
    if not request.user.is_authenticated: # verificando se o usuario esta logado ou não!
        return redirect('/home/home')
    
    if request.method == "GET":
        return render(request, 'tutor.html')
    if request.method == "POST":
        login, tutor, celular, estado, municipio = (
            request.POST.get(key) for key in ['usuario', 'tutor', 'celular', 'estado', 'municipio']
        )
        try:
            Tutor.objects.create(
                user=login,
                tutor=tutor,
                celular=celular,
                estado=estado,
                cidade=municipio
            )
            messages.success(request, 'Tutor registrado com sucesso.')
            return redirect('perfil/pet/')
        except Exception as e:
            messages.error(request, f'Erro ao registrar tutor: {str(e)}')
            return render(request, 'tutor.html', {'usuario': login})