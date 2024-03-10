from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="/"),
    
    path('termos/', views.termos, name="termos"),

    path('logar/', views.logar, name="logar"),




    path('cadastrar/', views.cadastrar, name="cadastrar"),
    
    path('entrar/', views.entrar, name='entrar'),

    path('realizando_cadastro/', views.realizando_cadastro, name="realizar_cadastro"),

    path('logout/', views.logout, name="logout"),
]