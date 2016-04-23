from django import forms
from .models import Registro
from django.contrib.admin import widgets

class RegistroForm(forms.ModelForm):

	class Meta:
		model = Registro

		fields = ["Arma",
					"no_casquillos",					
					"nombres",
					"apellidos",
					"edad",
					"muerto",
					"profesion",
					"cui",
					"sexo",
					"ubicacion",
					"fiscal",
					"fecha",
					"descripcion",
					"movil",
					"no_expediente",
					"Municipio",
												
			]

