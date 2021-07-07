from django.contrib import admin
from .models import *

# Register your models here.

class Solicitudadmin(admin.ModelAdmin):
    list_display=("empresa","rut","solicitante","producto","cantidad","categoria")

class Contratoadmin(admin.ModelAdmin):
    list_display=("empresa","rut","email","representante","fecha_inicio","fecha_termino")

admin.site.register(Solicitud, Solicitudadmin)
admin.site.register(Contrato, Contratoadmin)