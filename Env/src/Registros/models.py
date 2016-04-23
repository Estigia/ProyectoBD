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

	id = models.AutoField(primary_key=True)
	nombres = models.CharField(max_length=55, default = 'xx')
	apellidos = models.CharField(max_length=55, default = 'xx')
	edad = models.SmallIntegerField(blank=True, null=True)
	muerto = models.BooleanField(null=None)	
	profesion = models.CharField(max_length=45, blank=True, null=True)
	cui = models.CharField(max_length=13, blank=True, null= True)
	sexo = models.CharField(max_length=2,choices=Sexo_Choices, default='D')

	fiscal = models.CharField(max_length=60, blank=True, null=True)
	fecha = models.DateTimeField()
	fecha_registro = models.DateTimeField(auto_now=False, auto_now_add=True)
	descripcion = models.TextField()
	is_active = models.BooleanField(default = True)
	movil = models.CharField(max_length=100)
	no_expediente = models.CharField(max_length=40)
	Arma_id = models.ForeignKey('Armas.Arma', on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.id)
	

class Actividad(models.Model):
	id = models.AutoField(primary_key=True)
	Registro_id = models.ForeignKey('Registro',on_delete=models.CASCADE)
	Usuario_id = models.ForeignKey('home.Usuario',on_delete=models.CASCADE)
	actividad = models.CharField(max_length=45)

	verbose_name = 'Actividades'
