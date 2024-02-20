from django.shortcuts import render
# from django.http import HttpResponse

def cadastrar(request):
    return render(request, 'cadastro.html')