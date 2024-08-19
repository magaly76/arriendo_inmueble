from django.contrib import admin
from .models import Inmueble, TipoInmueble, Usuario, TipoUsuario, Comuna, EstadoPropiedad, RegistroArriendo, SolicitudArriendo

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(TipoInmueble)
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Comuna)
admin.site.register(EstadoPropiedad)
admin.site.register(RegistroArriendo)
admin.site.register(SolicitudArriendo)
