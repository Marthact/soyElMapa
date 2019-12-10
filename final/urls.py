
from django.contrib import admin
from django.urls import path
from django.conf import settings
from proyecto import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',v.inicio,name="inicio"),
    path('Salir/',v.salir_view,name="Salir"),
    path('registro/',v.registro_view,name="registro"),
    path('acceso/',v.acceso_view,name="acceso"),
  
    
]