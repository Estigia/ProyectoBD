from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Victima(models.Model):
	id = models.AutoField(primare_key=True)
	nombres = models.CharField(max_length=55)
	apellidos = models.CharField(max_length=55)
	edad = models.SmallIntegerField()
	muerto_herido = models.BooleanField(null=None)	
	profesion = models.CharField(max_length=45, blank=True, null=True)
	cui = models.CharField(max_length=13, blank=True, null= True)
	sexo = models.BooleanField(blank=True,null=None)

	def __unicode__(self):
		return self.nombres," ", self.apellidos

class Registro(models.Model)
	id = models.AutoField(primare_key=True)
	fiscal = models.CharField(max_length=60, blank=True, null=True)
	fecha = models.DateTimeField()
	descripcion = models.TextField()
	movil = models.CharField(max_length=100)
	no_expediente = models.CharField(max_length=40)
	Localizacion_id = models.ForeignKey('localizaciones.Localizacion', on_delete=models.CASCADE)
	Arma_id = models.ForeignKey('Armas.Arma', on_delete=models.CASCADE)
	Victima_id = models.ForeignKey('Victima', on_delete=models.CASCADE)

class Actividad(models.Model)
	id = models.AutoField(primary_key=True)
	Registro_id = models.ForeignKey('Registro',on_delete=models.CASCADE)
	Usuario_id = models.ForeignKey('home.Usuario',on_delete=models.CASCADE)
	actividad = models.CharField(max_length=45)
