from django.db import models




class Logro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    como_obtener = models.TextField()
    imagen = models.ImageField(upload_to='logros/')
    puntos = models.IntegerField()
    obtenido = models.BooleanField(default=False)  # Añadir este campo

    def __str__(self):
        return self.nombre