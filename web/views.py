from django.shortcuts import render
from .models import Comuna
from web.services import *

# Create your views here.
def indexView(request):
    comunas = obtener_comunas()
    return render (request, 'index.html',{'comunas':comunas})

def listado_inmueble(request):
    datos = obtener_inmueble_por_comuna()
    return render (request, 'index.html', {'datos':datos})