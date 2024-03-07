from django.db import models
from .articulo import Articulo




class Texto(models.Model):
    texto = models.TextField()
    lugar = models.IntegerField()
    articulo = models.ForeignKey(Articulo, on_delete = models.SET_NULL, null = True)