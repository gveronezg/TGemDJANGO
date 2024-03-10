from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants, add_message
from django.contrib import messages
from perfil.models import Tutor, Pet

import re

def feed(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "GET":
        tutorOK = Tutor.objects.filter(user_id=request.user.id).first()
        petOK = Pet.objects.filter(user_id=request.user.id).first()
        print("Tutor OK:", tutorOK)
        print("Pet OK:", petOK)
        if tutorOK and petOK:
            return render(request, 'feed.html')
        elif tutorOK:
            return redirect('/perfil/pet')
        else:
            return redirect('/perfil/tutor')