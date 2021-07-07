from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

def home(request):

    return render(request,"Maipo/home.html")


def extranjero(request):

    if request.method=="POST":
        
        subject=request.POST["nombre_empresa"]
        message=request.POST["rut"]+"\n"+request.POST["fecha_solicitud"]+"\n"+request.POST["solicitante"]+"\n"+request.POST["producto"]+"\n"+request.POST["cantidad"]+"\n"+request.POST["s_calidad"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["altomaipofrutas@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)

    return render(request, "Maipo/extranjero.html")
    
def nosotros(request):

    return render(request,"Maipo/nosotros.html")

def enviar_correo(request):

    if request.method=="POST":
        
        subject=request.POST["asunto"]
        message=request.POST["nombre"]+"\n"+request.POST["email"]+"\n"+request.POST["mensaje"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["altomaipofrutas@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
    
    return redirect(request.POST["pagina"])

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
  
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data
    )

    


