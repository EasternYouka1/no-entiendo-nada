from django.db import models
from django.contrib.auth.models import User

class info_usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    peso = models.IntegerField()
    edad = models.IntegerField()
    genero = models.CharField(max_length=1)
    altura = models.FloatField()
    litros_dia = models.IntegerField()
    comidas_dia = models.IntegerField()
    preferencias_alimentarias = models.CharField(max_length=200)
    nivel_actividad = models.IntegerField()
    primer_login = models.BooleanField(default=True)
    fecha_registro = models.DateField(auto_now_add=True)