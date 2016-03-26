from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Departamento(models.Model):
	id = models.AutoField(primary_key = True)
	departamento = models.CharField(max_length = 45)

class Municipio(models.Model):
	id = models.AutoField(primary_key = True)
	municipio = models.CharField(max_length = 45)
	Departamento_id = models.ForeignKey("Departamento", on_delete = models.CASCADE)

class Localizacion(models.Model):
	id = models.AutoField(primary_key = True)
	direccion = models.CharField(max_length = 100)
	especifico = models.BooleanField(blank=True, null=None)
	Municipio_id = models.ForeignKey("Municipio", on_delete =  models.CASCADE)
