from local.models import Producto
from django.db import models

# Create your models here.

class Subasta(models.Model):
    producto=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    destino=models.CharField(max_length=50)
    fecha_llegada=models.DateField()

    class Meta:
        verbose_name="Subasta"
        verbose_name_plural="Subastas"

class Puja(models.Model):
    nombre_empresa=models.CharField(max_length=50)
    rut=models.CharField(max_length=10)
    puja=models.FloatField()
    producto=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Puja"
        verbose_name_plural="Pujas"
    