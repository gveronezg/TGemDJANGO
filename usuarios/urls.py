from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    
    path('entrar/', views.entrar, name='entrar'),

    path('realizando_cadastro/', views.realizando_cadastro, name="realizar_cadastro"),
    path('logar/', views.logar, name="verificar_senha"),
    path('logout/', views.logout, name="logout"),
]