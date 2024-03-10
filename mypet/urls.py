from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('perfil/', include('perfil.urls')),
    path('feed/', include('feed.urls')),
    path('', lambda request: redirect('/')),
]