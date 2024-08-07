from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

tipoOficinaAmbiente = [
    ('Administrativo', 'Administrativo'),
    ('Formación', 'Formación')
]

tipoUsuario = [
    ('Administrativo', 'Administrativo'),
    ('Tecnico', 'Tecnico'),
    ('Empleado', 'Empleado'),
]

estadoCaso = [
    ('Solicitada', 'Solicitada'),
    ('En Proceso', 'En Proceso'),
    ('Finalizada', 'Finalizada')
]

tipoSolucion = [
    ('Parcial', 'Parcial'),
    ('Definitiva', 'Definitiva')
]


class OficinaAmbiente(models.Model):
    ofiTipo = models.CharField(max_length=15, choices=tipoOficinaAmbiente)
    ofiNombre = models.CharField(max_length=50, unique=True)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    fechaHoraActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.ofiNombre


class User(AbstractUser):
    userTipo = models.CharField(max_length=15, choices=tipoUsuario)
    userFoto = models.ImageField(upload_to="fotos/", null=True, blank=True)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    fechaHoraActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username


class Solicitud(models.Model):
    solUsuario = models.ForeignKey(User, on_delete=models.PROTECT)
    solDescripcion = models.TextField(max_length=1000)
    solOficinaAmbiente = models.ForeignKey(OficinaAmbiente, on_delete=models.PROTECT)
    fechaHoraCreacion = models.DateField(auto_now_add=True)
    fechaHoraActualizacion = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.solDescripcion


class Caso(models.Model):
    casSolicitud = models.ForeignKey(Solicitud, on_delete=models.PROTECT)
    casCodigo = models.CharField(max_length=20, unique=True)
    casUsuario = models.ForeignKey(User, on_delete=models.PROTECT)
    casEstado = models.CharField(max_length=15, choices=estadoCaso, default='Solicitada')
    fechaHoraActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.casCodigo}"


class TipoProcedimiento(models.Model):
    tipNombre = models.CharField(max_length=20, unique=True)
    tipDescripcion = models.TextField(max_length=1000, null=True)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    fechaHoraActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.tipNombre


class SolucionCaso(models.Model):
    solCaso = models.ForeignKey(Caso, on_delete=models.PROTECT)
    solProcedimiento = models.TextField(max_length=2000)
    solTipoSolucion = models.CharField(max_length=20, choices=tipoSolucion)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    fechaHoraActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.solTipoSolucion


class SolucionCasoTipoProcedimientos(models.Model):
    solSolucionCaso = models.ForeignKey(SolucionCaso, on_delete=models.PROTECT)
    solTipoProcedimiento = models.ForeignKey(TipoProcedimiento, on_delete=models.PROTECT)
