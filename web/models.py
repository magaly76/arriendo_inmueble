from django.db import models


class TipoUsuario(models.Model):
    id_tipou = models.SmallAutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombres = models.CharField(max_length=50)
    apellido_pat = models.CharField(max_length=50)
    apellido_mat = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    id_tipou = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipou')

    class Meta:
        managed = False
        db_table = 'usuario'

class Comuna(models.Model):
    comuna_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'comuna'


class EstadoPropiedad(models.Model):
    estprop_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_propiedad'


class TipoInmueble(models.Model):
    tipoi_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_inmueble'


class Inmueble(models.Model):
    inm_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_total = models.FloatField()
    nro_estacionamientos = models.IntegerField()
    nro_habitaciones = models.IntegerField()
    nro_banos = models.IntegerField()
    direccion = models.CharField()
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING)
    tipoi = models.ForeignKey(TipoInmueble, models.DO_NOTHING)
    precio_mensual = models.IntegerField(blank=True, null=True)
    estprop = models.ForeignKey(EstadoPropiedad, models.DO_NOTHING)
    rut = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='rut', related_name='inmuebles')

    class Meta:
        managed = False
        db_table = 'inmueble'


class RegistroArriendo(models.Model):
    registro_id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    estado_contrato = models.CharField(max_length=30, blank=True, null=True)
    inm = models.ForeignKey(Inmueble, models.DO_NOTHING, blank=True, null=True)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='registros_arriendo_as_arrendador')
    arrendatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='registros_arriendo_as_arrendatario')
    class Meta:
        managed = False
        db_table = 'registro_arriendo'


class SolicitudArriendo(models.Model):
    solicitud_id = models.AutoField(primary_key=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    estado_solicitud = models.CharField(max_length=30, blank=True, null=True)
    inm = models.ForeignKey(Inmueble, models.DO_NOTHING, blank=True, null=True)
    arrendatario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='rut', related_name='solicitudes_arriendo')

    class Meta:
        managed = False
        db_table = 'solicitud_arriendo'


