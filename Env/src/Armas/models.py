from __future__ import unicode_literals
from django.db import models

class Tipo_Arma(models.Model):
	id = models.AutoField(primary_key=True)
	objeto = models.CharField(max_length=45)

	def __unicode__():
		return objeto

class Arma(models.Model):
	id = models.AutoField(primary_key=True)
	calibre = models.CharField(max_length=20)	
	no_casquillos = models.SmallIntegerField(blank=True, null=True)
	marca = models.CharField(max_length=45, blank=True, null=True)
	categoria = models.BooleanField(blank=True, null=None)
	serial = models.CharField(max_length=45, blank=True,null=True)
	Tipo_Arma_id = models.ForeignKey('Tipo_Arma', on_delete=models.CASCADE);

