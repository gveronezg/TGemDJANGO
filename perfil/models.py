from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) # TODO: trocar o DO_NOTHING por deletar dados
    tutor = models.TextField(max_length=90)
    celular = models.IntegerField(max_length=12)
    ESTADO_ESCOLHIDO = (('AC', 'Acre'),('AL', 'Alagoas'),('AM', 'Amazonas'),('AP', 'Amapá'),('BA', 'Bahia'),('CE', 'Ceará'),('DF', 'Distrito Federal'),('ES', 'Espírito Santo'),('GO', 'Goiás'),('MA', 'Maranhão'),('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),('MT', 'Mato Grosso'),('PA', 'Pará'),('PB', 'Paraíba'),('PE', 'Pernambuco'),('PI', 'Piauí'),('PR', 'Paraná'),('RJ', 'Rio de Janeiro'),('RN', 'Rio Grande do Norte'),('RO', 'Rondônia'),('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),('SC', 'Santa Catarina'),('SE', 'Sergipe'),('SP', 'São Paulo'),('TO', 'Tocantins'))
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=2, choices=ESTADO_ESCOLHIDO)
    
    def __str__(self):
        return self.tutor
    
    