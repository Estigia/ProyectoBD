from __future__ import unicode_literals
from django.db import models

class Arma(models.Model):

	Categoria_Choices =(
			('Fg','Arma de Fuego'),
			('Bn','Arma Blanca'),
			('Ot','Otro'),
		)

	id = models.AutoField(primary_key=True)
	calibre = models.CharField(max_length=20, blank=True, null=True)	
	no_casquillos = models.SmallIntegerField(blank=True, null=True)
	marca = models.CharField(max_length=45, blank=True, null=True)
	categoria = models.CharField(max_length=2,choices=Categoria_Choices, default='Ot')
	objeto = models.CharField(max_length=45)
	serial = models.CharField(max_length=45, blank=True,null=True)
	
	def __unicode__(self):
		return self.objeto
