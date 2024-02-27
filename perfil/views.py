from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants, add_message
from django.contrib import messages

import re

def tutor(request):
    if not request.user.is_authenticated: # verificando se o usuario esta logado ou não!
        return redirect('/home/home')
    
    if request.method == "GET":
        return render(request, 'tutor.html')
