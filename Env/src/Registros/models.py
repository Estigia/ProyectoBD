from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registro(models.Model):	
	id = models.AutoField(primary_key=True)
	Sexo_Choices =(
			('M','Masculino'),
			('F','Femenino'),
			('D','Desconocido'),
		)
	
	nombres = models.CharField(max_length=55, default = 'xx')
	apellidos = models.CharField(max_length=55, default = 'xx')
	edad = models.SmallIntegerField(blank=True, null=True)
	muerto = models.BooleanField(null=None)	
	profesion = models.CharField(max_length=45, blank=True, null=True)
	cui = models.CharField(max_length=13, blank=True, null= True)
	sexo = models.CharField(max_length=2,choices=Sexo_Choices, default='D')
	ubicacion = models.TextField()

	no_casquillos = models.SmallIntegerField(blank=True, null=True)
	serial = models.CharField(max_length=45, blank=True,null=True)
	
	fiscal = models.CharField(max_length=60, blank=True, null=True)
	fecha = models.DateTimeField()
	fecha_registro = models.DateTimeField(auto_now=False, auto_now_add=True)
	descripcion = models.TextField()
	is_active = models.BooleanField(default = True)
	movil = models.CharField(max_length=100)
	no_expediente = models.CharField(max_length=40)

	def __unicode__(self):
		return str(self.id)

	def get_full_name(self):
		return self.nombres + " " + self.apellidos

	Municipio = models.ForeignKey('localizaciones.Municipio')
	Arma = models.ForeignKey('Armas.Arma')

	

class Actividad(models.Model):
	id = models.AutoField(primary_key=True)
	Registro_id = models.ForeignKey('Registro')
	Usuario_id = models.ForeignKey('home.Usuario')
	actividad = models.CharField(max_length=45)
	fecha = models.DateTimeField(auto_now=False,auto_now_add=True)

	verbose_name = 'Actividades'
