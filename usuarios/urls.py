from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="/"),
    path('termos/', views.termos, name="termos"),
    path('realizando_cadastro/', views.realizando_cadastro, name="realizar_cadastro"),
    path('logar/', views.logar, name="logar"),
    path('logout/', views.logout, name="logout"),
]