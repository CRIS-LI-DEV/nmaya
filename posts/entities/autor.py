from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    whatsapp  = models.CharField(max_length=100)
    email = models.CharField(max_length=1000)
