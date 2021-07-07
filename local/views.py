from django.shortcuts import render
from local.models import Producto,Calidad


# Create your views here.


def local(request):

    productos=Producto.objects.all()
    calidades=Calidad.objects.all()
    if request.GET.get('calidad')!=None:
        calidadGet=request.GET["calidad"]
        return render(request,"local/local.html", {"productos":productos, "calidades":calidades, "calidadGet":calidadGet})
    else:
        return render(request,"local/local.html", {"productos":productos, "calidades":calidades})