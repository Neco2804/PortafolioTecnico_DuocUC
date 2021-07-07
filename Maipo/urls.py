from django.urls import path
from Maipo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('extranjero', views.extranjero, name="extranjero"),
    path('enviar_correo', views.enviar_correo, name="enviar_correo"),
    path('registro', views.registro, name="registro"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)