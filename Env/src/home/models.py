from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tipo_Usuario (models.Model):
	id =  models.AutoField(primary_key=True) 
	nombre = models.CharField(max_length=45) 

	def __unicode__(self):
		return self.nombre

class Usuario (models.Model):
	id =  models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=55)
	apellidos = models.CharField(max_length=55)
	contrasena = models.CharField(max_length=32)
	institucion = models.CharField(max_length=30,blank=True)
	ultima_conexion = models.DateTimeField(auto_now_add=False, auto_now=True)
	nombre_usuario = models.CharField(max_length=20)
	correo = models.EmailField()
	Tipo_Usuario_id = models.ForeignKey('Tipo_Usuario',on_delete=models.CASCADE, default = 1)

	def __unicode__(self):
		return self.nombre

