from django.shortcuts import render
from .models import Subasta,Puja

# Create your views here.

def transporte(request):

    subastas=Subasta.objects.all()

    if request.POST.get('producto')!=None:
        pujaGet=request.POST
        INSERT=Puja(nombre_empresa=pujaGet["nombre_empresa"],rut=pujaGet["rut"],puja=float(pujaGet["puja"]),producto=pujaGet["producto"])
        INSERT.save()
    return render(request,"transporte/transporte.html", {"subastas":subastas})

