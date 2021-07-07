from django.db import models

# Create your models here.

class Solicitud(models.Model):
    id_solicitud=models.CharField(max_length=10)
    empresa=models.CharField(max_length=50)
    rut=models.CharField(max_length=50)
    solicitante=models.CharField(max_length=100)
    producto=models.CharField(max_length=100)
    cantidad=models.FloatField()
    categoria=models.CharField(max_length=50)
    
    class Meta:
        verbose_name="Solicitud"
        verbose_name_plural="Solicitudes"

class Contrato(models.Model):
    empresa=models.CharField(max_length=50)
    rut=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    representante=models.CharField(max_length=100)
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()

    class Meta:
        verbose_name="Contrato"
        verbose_name_plural="Contratos"