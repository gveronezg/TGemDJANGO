from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar, name="cadastrar")
]