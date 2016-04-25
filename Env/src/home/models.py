from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from datetime import datetime

# Create your models here.

class Tipo_Usuario (models.Model):
	id =  models.AutoField(primary_key=True) 
	nombre = models.CharField(max_length=45) 

	def __unicode__(self):
		return self.nombre

class UsuarioManager(BaseUserManager):

	def create_user(self, nombre_usuario, correo, nombre, apellidos, password=None):
		if not nombre_usuario:
			raise ValueError('Ingrese un nombre de usuario valido.')
		if not correo:
			raise ValueError('Ingrese una direccion de correo valida.')
		if not nombre:
			raise ValueError('Ingrese uno o mas nombres.')
		if not apellidos:
			raise ValueError('Ingrese sus apellidos.')

		usuario = self.model(
				nombre_usuario = nombre_usuario,
				correo = self.normalize_email(correo),
				nombre = nombre,
				apellidos = apellidos
			)

	 	usuario.set_password(password)
	 	usuario.save()

	 	return usuario

	def create_superuser(self, nombre_usuario,correo,nombre,apellidos, password=None):
	 	usuario = self.create_user(nombre_usuario,correo,nombre,apellidos,password)
	 	usuario.is_admin = True
	 	usuario.save()

	 	return usuario

class Usuario (AbstractBaseUser):
	id =  models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=55)
	apellidos = models.CharField(max_length=55)
	institucion = models.CharField(max_length=30,blank=True)
	ultima_conexion = models.DateTimeField(auto_now_add=False, auto_now=True)
	nombre_usuario = models.CharField(max_length=20, unique = True)
	correo = models.EmailField(unique = True)
	is_staff = models.BooleanField(default = True)
	is_active = models.BooleanField(default = True)
	Tipo_Usuario_id = models.ForeignKey('Tipo_Usuario', default = 1)

	verbose_name = 'Usuarios'

	objects = UsuarioManager()

	USERNAME_FIELD = 'nombre_usuario'
	REQUIRED_FIELDS = ['nombre','apellidos','correo']

	def get_full_name(self):
		return self.nombre+" "+self.apellidos

	def get_short_name(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre_usuario

	def has_module_perms(self,perm_list):
		return True

	def has_perm(self,perm):
		return True

