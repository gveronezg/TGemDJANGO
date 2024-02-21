from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('entrar/', views.entrar, name="entrar"),
    path('termos/', views.termos, name="termos"),
    path('concordar/', views.concordar, name="concordar"),
]