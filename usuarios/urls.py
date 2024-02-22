from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('logar/', views.logar, name="logar"),
    path('realizando_login', views.realizando_login, name="realizar_login")
]