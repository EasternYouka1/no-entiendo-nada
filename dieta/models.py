from django.db import models
from django.contrib.auth.models import User

class Comida(models.Model):
    TIPOS_COMIDA = [
        ('desayuno', 'Desayuno'),
        ('almuerzo', 'Almuerzo'),
        ('cena', 'Cena'),
        ('snack', 'Snack')
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    tipo_comida = models.CharField(max_length=20, choices=TIPOS_COMIDA)
    calorias = models.IntegerField()
    carbohidratos = models.FloatField()
    proteinas = models.FloatField()
    grasas = models.FloatField()
    fecha = models.DateField(auto_now_add=True)