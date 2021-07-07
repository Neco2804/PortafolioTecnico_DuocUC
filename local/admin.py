from django.contrib import admin
from .models import Producto, Calidad

# Register your models here.

class Productoadmin(admin.ModelAdmin):
    list_display=("nombre","calidad","precio","cantidad")
    readonly_fields=("created","updated")

class Calidadadmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

   
admin.site.register(Producto, Productoadmin)
admin.site.register(Calidad, Calidadadmin)