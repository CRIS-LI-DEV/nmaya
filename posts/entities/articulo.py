from django.db import models
from .autor import Autor

class Articulo(models.Model):
    titulo = models.CharField(max_length=1000)
    bajada = models.TextField()
    autor = models.ForeignKey(Autor,on_delete = models.SET_NULL, null=True)
    imagen_home = models.ImageField(upload_to='imagenes/')