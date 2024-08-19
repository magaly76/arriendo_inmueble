from .models import Comuna, TipoInmueble, TipoUsuario, EstadoPropiedad, Usuario, Inmueble,   RegistroArriendo, SolicitudArriendo
from datetime import date

def crear_comuna(comuna_id, nombre):
    comuna = Comuna(
        comuna_id=comuna_id,
        nombre=nombre
    )
    comuna.save()

def crear_tipo_inmueble(descripcion):
    tipo_inmueble=TipoInmueble(descripcion=descripcion)
    tipo_inmueble.save()

def crear_tipo_usuario(descripcion):
    tipo_usuario=TipoUsuario(descripcion=descripcion)
    tipo_usuario.save()

def crear_estado_propiedad(descripcion):
    estado_propiedad=EstadoPropiedad(descripcion=descripcion)
    estado_propiedad.save()

def crear_usuario(usu_rut, usu_nombre, usu_apellido_pat, usu_apellido_mat, usu_direccion, usu_telefono, usu_mail, id_tipou):
    tipou_codigo=TipoUsuario.objects.get(tipou_codigo=tipou_codigo)
    usuario= Usuario(
        usu_rut=usu_rut,
        usu_nombre= usu_nombre,
        usu_apellido_pat=usu_apellido_pat,
        usu_apellido_mat=usu_apellido_mat,
        usu_direccion=usu_direccion,
        usu_telefono=usu_telefono,
        usu_mail=usu_mail,
        id_tipou=id_tipou
    )
    usuario.save()

def crear_inmueble(nombre, descripcion, m2_construidos, m2_total, nro_estacionamientos, nro_habitaciones, nro_banos, direccion, comuna_id, tipoi_id, precio_mensual, estprop_id, rut):
    comuna= Comuna.objects.get(comuna_id=comuna_id)
    tipo_inmueble= TipoInmueble.objects.get(tipoi_id=tipoi_id)
    estado_propiedad = EstadoPropiedad.objects.get(estprop_id=estprop_id)
    arrendador = Usuario.objects.get(rut=rut, id_tipou__nombre='arrendador')

    inmueble=Inmueble(
        nombre=nombre,
        descripcion=descripcion,
        m2_construidos=m2_construidos,
        m2_total=m2_total,
        nro_estacionamientos=nro_estacionamientos,
        nro_habitaciones=nro_habitaciones,
        nro_banos=nro_banos,
        direccion=direccion,
        comuna_id= comuna,
        tipoi = tipo_inmueble,
        precio_mensual=precio_mensual,
        estprop_id = estado_propiedad,
        arrendador = arrendador
   )
    
    inmueble.save()
    return inmueble
    

def obtener_comunas():
     return Comuna.objects.all()
 
def actualizar(tipoi_id, descripcion):
    tipo_inmueble = TipoInmueble.objects.get(tipoi_id=tipoi_id)
    tipo_inmueble.descripcion = descripcion
    tipo_inmueble.save()

def borrar(comuna_id):
    comuna = Comuna.objects.get(comuna_id=comuna_id)
    comuna.delete()

def obtener_inmueble_por_comuna():
    datos = []
    comunas = Comuna.objects.all()
    for comuna in comunas:
        inmuebles = Inmueble.objects.filter(comuna=comuna)
        datos.append({
            'comuna': comuna.nombre,
            'inmuebles': inmuebles
        })
    return datos