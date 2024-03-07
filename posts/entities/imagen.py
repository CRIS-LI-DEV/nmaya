from django.db import models
from .articulo import Articulo


class Imagen(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.ImageField(upload_to='imagenes/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    lugar = models.IntegerField()
    articulo = models.ForeignKey(Articulo, on_delete = models.SET_NULL, null = True)

