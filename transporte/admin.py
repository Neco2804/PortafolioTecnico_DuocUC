from django.contrib import admin
from .models import Subasta, Puja

# Register your models here.

class Subastadmin(admin.ModelAdmin):
    list_display=("producto","cantidad","destino")

class Pujaadmin(admin.ModelAdmin):
    list_display=("nombre_empresa","rut","puja","producto")

admin.site.register(Subasta, Subastadmin)
admin.site.register(Puja, Pujaadmin)