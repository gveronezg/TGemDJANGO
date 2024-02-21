from django.shortcuts import render
# from django.http import HttpResponse

def cadastrar(request):
    return render(request, 'cadastrar.html')

def logar(request):
    return render(request, 'logar.html')