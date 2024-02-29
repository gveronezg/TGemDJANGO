from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('termos/', views.termos, name="termos"),
    
    path('validando_login/', views.validando_login, name="validar_login"),
    path('concordando/', views.concordando, name="checar_termos"),
]