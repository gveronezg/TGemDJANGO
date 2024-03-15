from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.usuario, name="usuario"),
    path('tutor/', views.tutor, name="tutor"),
    path('pet/', views.pet, name="pet"),
]