from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from django.core.validators import RegexValidator
cep_validator = RegexValidator(regex=r'^\d{8}$', message='CEP deve conter 8 dígitos numéricos.')

class Tutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) # TODO: trocar o DO_NOTHING por deletar dados
    tutor = models.CharField(max_length=100)
    celular = models.IntegerField(
        validators=[
            MaxValueValidator(99999999999),  # Máximo de 11 dígitos
            MinValueValidator(10000000000),  # Mínimo de 11 dígitos
        ]
    )
    cep = models.CharField(max_length=8, validators=[cep_validator])
    
    def __str__(self):
        return self.tutor