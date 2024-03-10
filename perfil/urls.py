from django.urls import path
from . import views

urlpatterns = [
    path('tutor/', views.tutor, name="tutor"),
]