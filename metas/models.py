from django.db import models
from django.contrib.auth.models import User

class MetaNutricional(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calorias_diarias = models.IntegerField(default=2000)
    carbohidratos_diarios = models.IntegerField(default=250) 
    proteinas_diarias = models.IntegerField(default=60)  
    grasas_diarias = models.IntegerField(default=70)     
    vasos_agua = models.IntegerField(default=8)
    veces_completadas = models.IntegerField(default=0)  

class ConsumoAgua(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vasos = models.IntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)