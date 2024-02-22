from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('logar/', views.logar, name="logar"),
    path('realizando_cadastro', views.realizando_cadastro, name="realizar_cadastro")
]