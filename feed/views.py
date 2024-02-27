from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants, add_message
from django.contrib import messages

import re

def feed(request):
    return render(request, 'feed.html')
