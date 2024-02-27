from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Tutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) # TODO: trocar o DO_NOTHING por deletar dados
    tutor = models.TextField(max_length=90)
    celular = models.IntegerField(
        validators=[
            MaxValueValidator(99999999999),  # Máximo de 11 dígitos
            MinValueValidator(10000000000),  # Mínimo de 11 dígitos
        ]
    )
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tutor